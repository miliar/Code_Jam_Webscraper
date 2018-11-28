/// Google Code Jam
/// Author   : Rajdip Saha
/// Language : C++

#include <bits/stdc++.h>

#define MAX 100005
#define INF 111111111111111111

typedef long long ll;
typedef unsigned long long llu;

using namespace std;

bool digit[15];

int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int t;
    char str[105];
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        scanf("%s",str);
        int len=strlen(str);
        int lo=0,hi=len-1;
        int res=0;
        while(lo<=hi){
            if(str[hi]=='-'){
                if(str[lo]=='+'){
                    for(int j=lo;str[j]!='-';j++)str[j]='-';
                    //cout<<str<<endl;
                    res++;
                }
                int in1=lo,in2=hi;
                while(in1<=in2){
                    //cout<<in1<<" "<<in2<<endl;
                    if(in1==in2){
                        bool flag=false;
                        if(str[in1]=='+')flag=true,str[in1]='-';
                        if(str[in1]=='-'&&!flag)str[in1]='+';
                    }
                    else{
                        bool flag1=false,flag2=false;
                        if(str[in1]=='+')flag1=true,str[in1]='-';
                        if(str[in1]=='-'&&!flag1)str[in1]='+';
                        if(str[in2]=='+')flag2=true,str[in2]='-';
                        if(str[in2]=='-'&&!flag2)str[in2]='+';
                    }
                    swap(str[in1],str[in2]);
                    //cout<<str<<endl;
                    in1++,in2--;
                }
                res++;
            }
            hi--;
        }
        printf("Case #%d: %d\n",i,res);
    }
    return 0;
}
