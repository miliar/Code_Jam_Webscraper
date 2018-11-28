#include<iostream>
#include<math.h>
#include<algorithm>
#include<string>
#include<string.h>
#include<vector>
#include<set>
#include<map>
#include<cstdio>
#include<queue>
#include<sstream>
#include<ctime>
using namespace std;

typedef long long ll;
typedef long long int lli;
#define mp make_pair
#define pb push_back

const int maxint=60000;

int main()
{
    freopen("inp.in", "r", stdin);
    freopen("inp.out", "w", stdout);
    int t;
    int digit[17];
    int r1,r2,number;
    int total;
    cin>>t;
    int start = 1;
    int chosen;
    while(start<=t){
        cin>>r1;
        total = 0;
        memset(digit,0,sizeof(digit));
        for(int i=1;i<=4;i++){
            for(int j=1;j<=4;j++){
                cin>>number;
                if(i==r1){
                    digit[number]++;
                }
            }
        }
        cin>>r2;
        for(int i=1;i<=4;i++){
            for(int j=1;j<=4;j++){
                cin>>number;
                if(i==r2 && digit[number]){
                    total++;
                    chosen = number;
                }
            }
        }
        if(total==1){
            cout<<"Case #"<<start<<": "<<chosen<<endl;
        }
        else if(total==0){
            cout<<"Case #"<<start<<": Volunteer cheated!"<<endl;
        }
        else cout<<"Case #"<<start<<": Bad magician!"<<endl;
        start++;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
