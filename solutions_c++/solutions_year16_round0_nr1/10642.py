#include <iostream>
#include <vector>
#include <cassert>
#include <cstdio>

using namespace std;
typedef long long ll;

void counting(int n);

int main() {
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;

    for(int i = 1; i <= T; i++){
        int N;
        cin >> N;
        cout << "Case #" << i << ": ";
        if(N==0) cout << "INSOMNIA\n";
        else counting(N);
    }
	return 0;
}

void counting(int n){
    int count = 2;
    bool sleep = false;
    //
    int temp = n;
    vector<int> tempDigits;
    vector<int> seenDigits;

    while(sleep != true){
        int sleepNum = temp;

        bool found = false;
        bool c0=false,c1=false,c2=false,c3=false,c4=false,c5=false,c6=false,c7=false,c8=false,c9=false;

        while(temp){
            tempDigits.push_back(temp%10);
            temp /= 10;
        }
        if(seenDigits.empty())
            seenDigits.push_back(tempDigits[0]);

        for(unsigned int i = 0; i < tempDigits.size(); i++){
            for(unsigned int j = 0; j < seenDigits.size(); j++){
                if(tempDigits[i] == seenDigits[j])
                    found = true;
                else
                    found = false;
            }
            if(found == false)
                seenDigits.push_back(tempDigits[i]);
        }

        for(unsigned int i = 0; i < seenDigits.size(); i++){
            if (seenDigits[i] == 0)
                c0 = true;
            else if (seenDigits[i] == 1)
                c1 = true;
            else if (seenDigits[i] == 2)
                c2 = true;
            else if (seenDigits[i] == 3)
                c3 = true;
            else if (seenDigits[i] == 4)
                c4 = true;
            else if (seenDigits[i] == 5)
                c5 = true;
            else if (seenDigits[i] == 6)
                c6 = true;
            else if (seenDigits[i] == 7)
                c7 = true;
            else if (seenDigits[i] == 8)
                c8 = true;
            else if (seenDigits[i] == 9)
                c9 = true;
        }


        if (c0==true&&c1==true&&c2==true&&c3==true&&c4==true&&c5==true&&c6==true&&c7==true&&c8==true&&c9==true){
            cout << sleepNum << endl;
            sleep = true;
        }
        else{
            temp = count*n;
            count++;

        }
    }//while loop end
}






