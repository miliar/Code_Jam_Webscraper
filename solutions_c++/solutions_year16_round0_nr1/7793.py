#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	int t=0,j,pos=0,count=0;
	bool flag=false;
	int n=0,num=0,num2=0,i,last,k;
	int a[10];
	ifstream fin;
	fin.open("input.txt");
	ofstream fout;
	fout.open("output.txt");
	fin>>t;
	while(t>0)
	{
		count++;
		pos=0;
		fin>>n;
	  
	    if(n==0)
	            fout<<"case #"<<count<<": INSOMNIA\n";
        else
        {
	    	for(k=0;k<10;k++)
    			a[k]=-1;
                	
    		for(i=1;;i++)
    		{
    			num=num2=i*n;
    			while(num>0)
    			{
    				last=num%10;
    				for(j=0;j<10;j++)
    				{
    					if(last==a[j]){ flag=false; break;}
    					else { flag=true;}
    				}
    				if(flag==true)
    				{
    					a[pos]=last;
    					pos++;	
    					flag=false;
    				}
    				num=num/10;
    			}
    
    			if(pos==10)
    				break;
    		}
    		fout<<"case #"<<count<<": "<<num2<<endl;
      }
		t--;
	}	
	return 0;
}
