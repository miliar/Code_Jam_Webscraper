#include<iostream>
#include<fstream>
 
 using namespace std;
int main()
{
 ifstream fin("A1.txt");
 ofstream fout("output.txt");
 int n,arr[4][4],arr1[4][4],p=0,q=0,i=0,j,k,count=0,a=0,b=0;
 fin>>n;
 for(i=0;i<n;i++)
  {
    count=0;
     a=0;
     fin>>p;
       for(j=0;j<4;j++)
	 for(k=0;k<4;k++)
	   {fin>>arr[j][k];
	   }
     fin>>q;
	for(j=0;j<4;j++)
	 for(k=0;k<4;k++)
	   {fin>>arr1[j][k];
	   }
   for(k=0;k<4;k++)
    { a=arr[p-1][k];
      for(j=0;j<4;j++)
	{ if(a==arr1[q-1][j])
	   { count=count+1;
	     b=a;
	   }
	}
    }
     if(count==1)
       {fout<<"Case #"<<i+1<<": "<<b<<"\n";
       }
     if(count>1)
       {fout<<"Case #"<<i+1<<": Bad magician!\n";
       }
     if(count==0)
       {fout<<"Case #"<<i+1<<": Volunteer cheated!\n";
       }

 }
 return 0;
}




