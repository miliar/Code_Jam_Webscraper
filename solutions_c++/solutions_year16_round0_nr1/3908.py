#include <bits/stdc++.h>
using namespace std;
bool seen[10];
void getdigs(int n){
    do {
        int digit = n % 10;
        seen[digit] = true;
        n /= 10;
    } while (n > 0);
}
int main()
{
    freopen("sheep.in","r",stdin);
    freopen("sheep.out","w",stdout);
    int t;
    int myval;
    scanf("%d",&t);
    for(int i=0;i<t;i++){
        scanf("%d",&myval);
        for(int j=0;j<10;j++){
            seen[j] = false;
        }
        int otherval = myval;
        bool done = false;
        if(myval == 0){
            cout << "CASE" << " " << "#" << i+1 << ":" << " " << "INSOMNIA" << endl;
        }
        else{
            while(true){
                getdigs(otherval);
                bool whatevs = true;
                for(int j=0;j<10;j++){
                    if(!seen[j])whatevs=false;
                }
                if(whatevs){
                    done = true;
                    cout << "CASE" << " " << "#" << i+1 << ":" << " " << otherval << endl;
                    break;
                }
                else{
                    otherval += myval;
                }
            }
        }
    }
    return 0;
}
