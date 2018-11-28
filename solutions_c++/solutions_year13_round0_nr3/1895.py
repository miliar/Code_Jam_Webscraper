#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;

int w1,w2,z;
string s1,s2,s3,s;
char ch;

int  findpal()
{
    int i=0,j=z-1,k,m,i1,j1;
    for(;s1[i]=='0';i++);
    i1=i;j1=j;
   for(;i<=j;i++,j--)
    if(s1[i]>=s1[j]) s1[j]=s1[i];
   else break;
   if(i<=j)
   {
       k=(i1+j1)/2;
       while(k>=0&&s1[k]=='9') s1[k--]='0';
       if(k<0) return -1;
       s1[k]++;
       if(k<i1) i1=k;
       for(;i1<=j1;i1++,j1--) s1[j1]=s1[i1];

   }
    return 0;


}

int findnextpal()
{
    int i=0,j=z-1,k,m;
    for(;s1[i]=='0';i++);
    k=(i+j)/2;m=(i+j+1)/2;//check
    while(k>=0&&s1[k]=='9')
    {
        s1[k]='0';s1[m]=s1[k];k--;m++;
    }
    if(k<0) return -1;
    s1[k]++;s1[m]=s1[k];
    if(k<i)
    {
        s1[k]='1';k++;
        for(;k<z-1;k++) s1[k]='0';
        s1[k]='1';
    }
    return 0;


}
bool sqrpalin()
{
    int n1=0,i=0,j;
    for(;s[i]=='0';i++);
    for(;i<z;i++)
        n1=n1*10+s1[i]-'0';
    long long num=n1;
    num=num*num;
    s="";
    while(num!=0)
    {
        s+=num%10+'0';num/=10;
    }
    i=0;j=s.length()-1;
    for(;i<=j&&s[i]==s[j];i++,j--);
    if(i<=j) return 0;
    return 1;


}

long long findpalc()
{
    int i;
    long long c=0;
    s3="";s1="";s2="";
    while(w2!=0)
    {
        s3+=(w2%10+'0');
        w2/=10;
    }
    for(i=s3.length()-1;i>=0;i--)s2+=s3[i];
    z=s3.length();s3="";
    while(w1!=0)
    {
        s3+=(w1%10+'0');
        w1/=10;
    }
    for(i=z-s3.length();i>0;i--) s1+='0';
    for(i=s3.length()-1;i>=0;i--)s1+=s3[i];
    //cout<<s1<<endl<<s2<<endl;

    if(findpal()==-1) return 0;//find first palindrome---forget starting zeroes
    //cout<<s1<<endl;
    while(s1<=s2)
    {
       if(sqrpalin()) c++;
        if(findnextpal()==-1) return c;
        //cout<<s1<<endl;
    }
    return c;



}

int main()
{
    int t,w;
    long long a,b,r;
    scanf("%d",&t);

    for(w=1;w<=t;w++)
    {
        scanf("%lld%lld",&a,&b);
        //cout<<a<<" "<<b<<endl;
        w1=ceil(sqrt(a));
        w2=sqrt(b);
        //cout<<"w"<<w1<<" "<<w2<<endl;
        r=findpalc();
        //cout<<"r"<<r<<endl;
        printf("Case #%d: %lld\n",w,r);
    }

}


