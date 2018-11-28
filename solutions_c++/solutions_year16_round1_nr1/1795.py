#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int i,T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        string s;
        char a[5000];
        int l,r;
        cin>>s;
        l=r=2500;
        a[l]=s[0];
        for(i=1;i<s.length();i++){
            if(s[i]>=a[l]){
                l--;
                a[l]=s[i];
            }else{
                r++;
                a[r]=s[i];
            }
        }
        a[++r]='\0';
        printf("Case #%d: %s\n",t,a+l);
        //for(i=l;i<=r;i++)
            //cout<<

    }
    return 0;
}
