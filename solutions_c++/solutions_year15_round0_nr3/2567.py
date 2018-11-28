#include<stdio.h>
#include<iostream>
#include<map>
#include<string>

#include<string.h>
using namespace std;
int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("outOfc2Final1.txt","w", stdout);
    //1,-1
    //arr[4][4]={{'1','i','j','k'},{'i','a','k','b'},{'j','c','d','i'},{'k','j','a','d'}};
    map<pair<char,char>,string> m;
   /* m[pair<string,string>("1","1")]="1";
    m[pair<string,string>("1","i")]="i";
    m[pair<string,string>("1","j")]="j";
    m[pair<string,string>("1","k")]="k";
    m[pair<string,string>("i","1")]="i";
    m[pair<string,string>("i","i")]="-1";
    m[pair<string,string>("i","j")]="k";
    m[pair<string,string>("i","k")]="-j";
    m[pair<string,string>("j","1")]="j";
    m[pair<string,string>("j","i")]="-k";
    m[pair<string,string>("j","j")]="-1";
    m[pair<string,string>("j","k")]="i";
    m[pair<string,string>("k","1")]="k";
    m[pair<string,string>("k","i")]="j";
    m[pair<string,string>("k","j")]="-i";
    m[pair<string,string>("k","k")]="-1";*/
    m[pair<char,char>('1','1')]="+1";
    m[pair<char,char>('1','i')]="+i";
    m[pair<char,char>('1','j')]="+j";
    m[pair<char,char>('1','k')]="+k";
    m[pair<char,char>('i','1')]="+i";
    m[pair<char,char>('i','i')]="-1";
    m[pair<char,char>('i','j')]="+k";
    m[pair<char,char>('i','k')]="-j";
    m[pair<char,char>('j','1')]="+j";
    m[pair<char,char>('j','i')]="-k";
    m[pair<char,char>('j','j')]="-1";
    m[pair<char,char>('j','k')]="+i";
    m[pair<char,char>('k','1')]="+k";
    m[pair<char,char>('k','i')]="+j";
    m[pair<char,char>('k','j')]="-i";
    m[pair<char,char>('k','k')]="-1";
    int t;
    cin>>t;
    char a[10005];
    char b[10005];
    long long l,x;
    int ab=1;
    while(t--)
    {
        cin>>l>>x;
        cin>>a;

        int j=0;
        int i=0;
        int m1=0;
       //3 cout<<a[0];
        for(m1=0;m1<x;m1++){
        for(i=0;i<l;i++)
        {
            b[j++]=a[i];
        }
        }
        int start=0,count=0;
        char ans[2];
        ans[0]='+';
        ans[1]='1';
        char temp=ans[0];
         //ans
        for(i=0;i<l*x;i++)
        {
            temp=ans[0];
            //cout<<temp<<"abc";
            ans[0]=m[make_pair(ans[1],b[i])][0];
            ans[1]=m[make_pair(ans[1],b[i])][1];
            //cout<<ans[0]<<"a"<<ans[1]<<"b";
            //std::string s;s = s + b[i];
            if(temp=='-'&&ans[0]=='-')
                ans[0]='+';
            else if(temp=='-'||ans[0]=='-')
                ans[0]='-';
            if(ans[0]=='+'&&ans[1]=='i'&&count==0){
                count=1;
                ans[0]='+';
                ans[1]='1';
            }
            if(ans[0]=='+'&&ans[1]=='j'&&count==1){

                count=2;
                ans[0]='+';
                ans[1]='1';
            }
        }
       // cout<<ans[0]<<ans[1];
        if(count==2&&i==(l*x)&&ans[0]=='+'&&ans[1]=='k')
            printf("Case #%d: YES",ab);

        else
            printf("Case #%d: NO",ab);
             printf("\n");
         ab++;


    }
    return 0;
}
