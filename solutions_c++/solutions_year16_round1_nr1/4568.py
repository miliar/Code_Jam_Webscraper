int t;
cin>>t;
int q=0;
while(t>0)
{
t--;
q++;
char s[1005];
cin>>s;
int p=strlen(s);
int j=p-1;
int k=p+1;
char c[2*p+1];
c[p]=s[0];
char max=c[p];
for(int i=1;i<p;i++)
{
if(s[i]>=max)
{c[j]=s[i];
max=c[j];
j--;
}
else
{c[k]=s[i];
k++;
}
}
int l=0;
char h[p+1];
for(int i=0;i<=2*p+1;i++)
{
if(c[i]<='Z'&&c[i]>='A')
{
h[l]=c[i];
l++;
}
}
cout<<"Case #"<<q<<": ";
for(int i=0;i<p;i++)
{
cout<<h[i];
}
cout<<endl;
}
