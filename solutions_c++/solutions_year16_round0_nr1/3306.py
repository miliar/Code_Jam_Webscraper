#include <fstream>
using namespace std;

int check(int arr[])
{
   for(int i=0;i<10;i++)
   if(arr[i]==0)
   return 0;
   return 1;
}

int main() {
    fstream fin;
    fstream fout;
    fin.open("input.in",ios::in);
    fout.open("output.out",ios::out);
	int t,n,m,o,l,i;
	int flag;
	fin>>t;
	for(int j=1;j<=t;j++)
	{
	    fin>>m;
	    if(m==0){
	    fout<<"Case #"<<j<<": INSOMNIA"<<endl;
	    continue;
	    }
	    int a[10];
	    for(l=0;l<10;l++)
	    a[l]=0;
	    n=m;
	    i=1;
	    flag=0;
	    while(1)
	    {
	        o=n;
	        while(o!=0)
	        {
	            a[o%10]++;
	            o/=10;
	        }
	        flag=check(a);
	        if(flag==1)
	        break;
	        i++;
	        n=m*i;
	    }
	    fout<<"Case #"<<j<<": "<<n<<endl;
	}
	return 0;
}
