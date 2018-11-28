#include<iostream>
#include<string.h>
#include<cstdio>

using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);

    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);

    int t;
    cin >> t;
    char shyne[1001];
    int MAX;
    for(int j=1;j<=t;j++){
        cin >> MAX;
        cin >> shyne;
        int stup=0;
        int invite=0;
        if(shyne[0]-'0'==0){invite++;stup++;}
        else {stup=stup+shyne[0]-'0';}
        for(int i=1;i<strlen(shyne);i++){
            if(shyne[i]-'0'>0 && i<=stup){stup=stup+shyne[i]-'0';}
            else if(shyne[i]-'0'>0 && i>stup){invite=invite+(i-stup);stup=stup+(i-stup)+shyne[i]-'0';}
        }
        cout << "Case #" << j << ": " << invite << "\n";
    }
}
