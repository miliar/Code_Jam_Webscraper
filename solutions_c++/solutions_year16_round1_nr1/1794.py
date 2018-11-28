#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
    //freopen("out.txt","w",stdout);
    int t;

    char buffer[1001];
    scanf("%d",&t);
    for(int i=0;i<t;i++){
        scanf("%s",buffer);
        printf("Case #%d: ",i+1);
        string s="";
        int l=(int)strlen(buffer);
        for(int j=0;j<l;j++){
            if(s=="")s+=buffer[j];
            else{
                if(s[0]<=buffer[j])s=buffer[j]+s;
                else s+=buffer[j];
            }
        }
        cout<<s<<endl;
    }
    return 0;
}
