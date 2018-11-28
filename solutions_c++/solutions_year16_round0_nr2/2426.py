#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#define LENGTH 101
#define POS 0
#define NEG 1
using namespace std;
int a[LENGTH][2];
char ss[LENGTH];
void shorten(int in[LENGTH],int in_length,int out[LENGTH],int &out_length);
int main()
{
    int cas;
    int str[LENGTH];
    int str2[LENGTH];
    int str3[LENGTH];
    freopen("B-large.in","r",stdin);
    freopen("Bout.txt","w",stdout);
    for(int i =0;i<LENGTH;i++)
        for(int j = 0 ;j<2;j++)a[i][j] = LENGTH;
    a[1][POS] = 0;
    a[1][NEG]= 1;

    for(int i = 2 ; i< LENGTH;i++){
        for(int j = 0 ;j < 2 ;j++){
                int t= j;
            for(int k = 0 ; k < i ; k++){
                    str[k] = t;
                    t = (t+1)%2;
            }
            int ans = -1;
            int l3;

            for(int l = 0;l<i;l++)str2[l] =str[l];
            shorten(str2,i,str3,l3);

            if(l3 < i){
                if(str3[0] == 0) a[i][j] = min(a[i][j],a[l3][POS]);
                else a[i][j] = min(a[i][j],a[l3][NEG]);
            }

            for(int k = 0 ;k < i;k++){
                for(int l =0;l<=k;l++)str2[l] = (str[k-l]+1)%2;
                for(int l =k+1;l<i;l++)str2[l] = str[l];

                shorten(str2,i,str3,l3);
                if(l3 < i){
                    if(str3[0] == 0) a[i][j] = min(a[i][j],a[l3][POS]+1);
                    else a[i][j] = min(a[i][j],a[l3][NEG]+1);
                }
            }
        }
    }

    cin>>cas;
    for(int q=1;q<=cas;q++){
        cin>>ss;
        int len = strlen(ss);
        int olen;
        for(int i = 0 ;i < len ; i++){
            if(ss[i] == '+')str[i] = 0; else str[i] = 1;
        }
        shorten(str,len,str2,olen);
        cout<<"Case #"<<q<<": ";
        if(str2[0]==0)cout<<a[olen][POS]<<endl;
        else cout<<a[olen][NEG]<<endl;
    }
    return 0;
}
void shorten(int in[LENGTH],int in_length,int out[LENGTH],int &out_length)
{
    out_length = 0;
    for(int l =0;l<in_length;){
        int start = l;
        while(l<in_length && in[start] == in[l])l++;
        out[out_length++] = in[start];
    }
}
