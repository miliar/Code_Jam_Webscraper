# include"iostream"
# include"string"
# include<stdio.h>
using namespace std;

int main()
{

int i,j=0,t,l,s[1001];
cin>>t;
while(j++<t)
{
int sum=0,ppl=0;
scanf("%d",&l);
string s1;
cin>>s1;
for(i=0;i<l+1;i++)
{
if(sum<i&&(s1[i]-48)>0)
{
ppl=ppl+i-sum;
sum=sum+ppl;
}
sum=sum+s1[i]-48;

}


cout<<"case #"<<j<<":"<<" "<<ppl<<endl;
}

return 0;
}
