#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
#define LLD long int
bool isCON(char Ch)
{
    if(Ch=='a' || Ch=='e' || Ch=='i' || Ch=='o' || Ch=='u')
        return false;
    return true;
}
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int i, j, k, n,  tCase, nCase=1;
    char S[1000006];
    cin >> tCase;
    while(tCase--)
    {
        cin >> S >> n;
        int len = strlen(S);
        int cnt=0, count=0;
        LLD ans=0;
        int last = -1;
       for(i=0; i<len; i++)
       {
           if(isCON(S[i])==true) cnt++;
           else cnt=0;

           if(cnt>=n)
           {
               LLD left = (i-n) - last;
               if(cnt == n && i==n-1)
                    left = 0;
               LLD right = len-i-1;
               //cout << left <<" " <<right << " " <<endl;
               ans+= left + right + left*right + 1;
               last = i-n+1;
           }
       }
       cout << "Case #" << nCase++ << ": "<<ans << endl;

    }
    return 0;

}


