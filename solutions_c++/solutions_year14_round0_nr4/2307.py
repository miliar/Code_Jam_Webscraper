#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>

using namespace std;
int caseNum;

void solve(){
int n;
int start1,start2,end1,end2;
cin >> n;

double a1[n];
double a2[n];
int points1 = 0;
int points2 = 0;
for(int i = 0; i < n;i++){
    cin >> a1[i];
}
for(int i = 0; i < n;i++){
    cin >> a2[i];
}
start1 = 0;
start2 = 0;
end1 = n-1;
end2 = n-1;
sort(a1,a1+n);
reverse(a1,a1+n);
sort(a2,a2+n);
reverse(a2,a2+n);

for(int i = 0; i < n; i++){
    if(a1[start1] > a2[start2]){
        points1++;
        start1++;
        start2++;
    }
    else{
        start2++;
        end1--;
    }

}


start1 = 0;
start2 = 0;
end1 = n-1;
end2 = n-1;
for(int i = 0; i < n; i++){
    if(a1[start1] > a2[start2]){
        points2++;
        start1++;
        end2--;
    }
    else{
        start2++;
        start1++;
    }

}


cout << "Case #"<< caseNum++ << ": " << points1 << " " << points2<<endl;
}
int main(){
int t;
caseNum=1;
cin >> t;
for(int i = 0; i < t; i++){
solve();

}
}

/*
//determines if a farm should be bought

int a,b,c;

void solve(){
bool solution = false;
bool noC = true;
int board[a][b];

for(int i = 0; i < a; i++)
    for(int j = 0; j < b;j++)
        board[i][j] = 0;

if(c >= a*b){

}
else{
for(int i = 0; i < a*b; i ++){
    if(i < c)
    board[i/b][i%b]= -1;
    else{
        int slot1=i/b;
        int slot2=i%b;
        bool oneUpA = false,twoUpA = false,oneDownA = false,twoDownA = false;
        if(slot1+1< a){
            oneUpA = true;
        }
        if(slot1-1 >=0)
            oneDownA = true;
        if(slot2+1< b){
            twoUpA = true;
        }
        if(slot2-1 >=0)
            twoDownA = true;

        if(oneUpA){
            if(board[slot1+1][slot2] == -1){
                board[slot1][slot2] = 1;
                continue;
            }
            if(twoDownA){
                if(board[slot1+1][slot2-1] == -1){
                board[slot1][slot2] = 1;
                continue;
            }
            }
            if(twoUpA){
                if(board[slot1+1][slot2+1] == -1){
                board[slot1][slot2] = 1;
                continue;
            }
            }

        }
        if(oneDownA){
            if(board[slot1-1][slot2] == -1){
                board[slot1][slot2] = 1;
                continue;
            }
            if(twoDownA){
                if(board[slot1-1][slot2-1] == -1){
                board[slot1][slot2] = 1;
                continue;
            }
            }
            if(twoUpA){
                if(board[slot1-1][slot2+1] == -1){
                board[slot1][slot2] = 1;
                continue;
            }
            }
        }
        if(twoUpA){
            if(board[slot1][slot2+1] == -1){
                board[slot1][slot2] = 1;
                continue;
            }

        }
        if(twoDownA){
            if(board[slot1][slot2-1] == -1){
                board[slot1][slot2] = 1;
                continue;
            }
        }

    }
}


//check for solution
solution = true;
for(int i = 0; i < a; i++){
    for(int j = 0; j < b; j++){
        if(board[i][j] == 1){
            int slot1 = i;
            int slot2 = j;
            bool oneUpA = false,twoUpA = false,oneDownA = false,twoDownA = false;
            if(i+1< a){
                oneUpA = true;
            }
            if(i-1 >=0)
                oneDownA = true;
            if(j+1< b){
                twoUpA = true;
            }
            if(j-1 >=0)
                twoDownA = true;

                if(oneUpA){
            if(board[slot1+1][slot2] == 0){

                continue;
            }
            if(twoDownA){
                if(board[slot1+1][slot2-1] == 0){

                continue;
            }
            }
            if(twoUpA){
                if(board[slot1+1][slot2+1] == 0){

                continue;
            }
            }

        }
        if(oneDownA){
            if(board[slot1-1][slot2] == 0){

                continue;
            }
            if(twoDownA){
                if(board[slot1-1][slot2-1] == 0){

                continue;
            }
            }
            if(twoUpA){
                if(board[slot1-1][slot2+1] == 0){

                continue;
            }
            }
        }
        if(twoUpA){
            if(board[slot1][slot2+1] == 0){

                continue;
            }

        }
        if(twoDownA){
            if(board[slot1][slot2-1] == 0){

                continue;
            }
        }


            solution = false;
        }
    }
}


if(!solution){

for(int i = 0; i < a; i++)
    for(int j = 0; j < b;j++)
        board[i][j] = 0;
for(int i = 0; i < a*b && !solution; i ++){
    if(i < c)
    board[i%a][i/a]= -1;
    else{
        int slot1=i%a;
        int slot2=i/a;
        bool oneUpA = false,twoUpA = false,oneDownA = false,twoDownA = false;
        if(slot1+1< a){
            oneUpA = true;
        }
        if(slot1-1 >=0)
            oneDownA = true;
        if(slot2+1< b){
            twoUpA = true;
        }
        if(slot2-1 >=0)
            twoDownA = true;

        if(oneUpA){
            if(board[slot1+1][slot2] == -1){
                board[slot1][slot2] = 1;
                continue;
            }
            if(twoDownA){
                if(board[slot1+1][slot2-1] == -1){
                board[slot1][slot2] = 1;
                continue;
            }
            }
            if(twoUpA){
                if(board[slot1+1][slot2+1] == -1){
                board[slot1][slot2] = 1;
                continue;
            }
            }

        }
        if(oneDownA){
            if(board[slot1-1][slot2] == -1){
                board[slot1][slot2] = 1;
                continue;
            }
            if(twoDownA){
                if(board[slot1-1][slot2-1] == -1){
                board[slot1][slot2] = 1;
                continue;
            }
            }
            if(twoUpA){
                if(board[slot1-1][slot2+1] == -1){
                board[slot1][slot2] = 1;
                continue;
            }
            }
        }
        if(twoUpA){
            if(board[slot1][slot2+1] == -1){
                board[slot1][slot2] = 1;
                continue;
            }

        }
        if(twoDownA){
            if(board[slot1][slot2-1] == -1){
                board[slot1][slot2] = 1;
                continue;
            }
        }
        board[slot1][slot2] = 0;
    }
}

solution = true;
for(int i = 0; i < a; i++){
    for(int j = 0; j < b; j++){
        if(board[i][j] == 1){
            int slot1 = i;
            int slot2 = j;
            bool oneUpA = false,twoUpA = false,oneDownA = false,twoDownA = false;
            if(i+1< a){
                oneUpA = true;
            }
            if(i-1 >=0)
                oneDownA = true;
            if(j+1< b){
                twoUpA = true;
            }
            if(j-1 >=0)
                twoDownA = true;

                if(oneUpA){
            if(board[slot1+1][slot2] == 0){

                continue;
            }
            if(twoDownA){
                if(board[slot1+1][slot2-1] == 0){

                continue;
            }
            }
            if(twoUpA){
                if(board[slot1+1][slot2+1] == 0){

                continue;
            }
            }

        }
        if(oneDownA){
            if(board[slot1-1][slot2] == 0){

                continue;
            }
            if(twoDownA){
                if(board[slot1-1][slot2-1] == 0){

                continue;
            }
            }
            if(twoUpA){
                if(board[slot1-1][slot2+1] == 0){

                continue;
            }
            }
        }
        if(twoUpA){
            if(board[slot1][slot2+1] == 0){

                continue;
            }

        }
        if(twoDownA){
            if(board[slot1][slot2-1] == 0){

                continue;
            }
        }
            solution = false;
        }
    }
}

}


if(!solution){
    //start building a sqaure in the top left
}

if(!solution){
    //start building a sqaure in the top left
}
}
cout << "Case #" << caseNum << ":"  << endl;
if(solution){
    for(int i = 0; i < a; i++){
        for(int j = 0; j < b;j++){
            if(board[i][j]== -1)
                cout << '*';
            else if(board[i][j] == 0 && noC){
                cout << 'c';
                noC = false;
            }
            else{
                cout << '.';
            }
        }

        cout << endl;

    }
}
else
    cout << "Impossible" << endl;
caseNum++;
}


int main(){
caseNum = 1;
int t;
cin >> t;
for(int i = 0; i < t;i++){
cin >> a >> b >> c;
solve();

}


}
*/
