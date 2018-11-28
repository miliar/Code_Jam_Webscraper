#include<iostream>
#include<fstream> 	
long int length();
char name[1000000];
using namespace std;
int main()
{
ifstream fin("input.in",ios::in);
ofstream fout("output",ios::out);
long int n;
long int T;
fin>>T;
long int arr[1000000];
for(long int t=0;t<T;t++)
{
fin>>name;
fin>>n;
// cout<<"n="<<n<<"\n";
long int nl=length();
long int k=0;
  for(long int i=0;i<=nl-n;i++)
  {
   
     int flag=0;
     for(long int j=i;j<i+n;j++)
        { 
	   if( name[j]=='a' || name[j]=='e' || name[j]=='i' || name[j]=='o' || name[j]=='u' ) break;
	   else flag++;
	   if(flag==n) { arr[k]=i; k++; }
	}
   
  }
// cout<<"k="<<k<<"\n";

long int start=0;
long   int count=0;
for(long int i=0;i<k;i++)
{
// cout<<"arr[i]="<<arr[i]<<"\n";
if( (arr[i]-start+1)==0 ) count+=(nl-arr[i]);
else if( (nl-arr[i])==0 ) count+=(arr[i]-start+1);
else count+=( (arr[i]-start+1) * (nl-arr[i]-n+1) );
start=arr[i]+1;
// cout<<"count+="<<((arr[i]-start+1) * (nl-arr[i]))<<"\n";
}

fout<<"Case #"<<t+1<<": "<<count<<"\n";
  
}
return 0;
}

long int length()
{
long int i;
for(i=0;name[i]!='\0';i++) {}
// cout<<"length="<<i<<"\n";
return i;
}
