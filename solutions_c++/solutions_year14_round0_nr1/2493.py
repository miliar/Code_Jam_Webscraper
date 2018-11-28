#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int caseNum;
void trashLine(){
int trash;
cin >> trash;
cin >> trash;
cin >> trash;
cin >> trash;
}

void solve(){
int line;
int set1[4];
int set2[4];
cin >> line;
line--;
for(int i = 0; i < 4; i++){
if(i == line){
    for(int j = 0; j < 4;j++)
    cin >> set1[j];
}
else
    trashLine();

}
cin >> line;
line--;
for(int i = 0; i < 4; i++){
if(i == line){
    for(int j = 0; j < 4;j++)
    cin >> set2[j];
}
else
    trashLine();

}

vector<int> matchs;

for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            if(set1[i] == set2[j])
                matchs.push_back(set1[i]);

if(matchs.size()==0){
    cout << "Case #" << caseNum << ": " << "Volunteer cheated!" << endl;
}
else if(matchs.size()==1)
cout << "Case #" << caseNum << ": " << matchs[0] << endl;
else
cout << "Case #" << caseNum << ": " << "Bad magician!" << endl;

caseNum++;
}

int main(){
caseNum = 1;
int t;
cin >> t;
for(int i = 0; i < t;i++){

solve();

}


}
