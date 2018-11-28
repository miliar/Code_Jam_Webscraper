#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
    int size,t,i,j,end_plus,beg_minus,count,j1,count1;
    char temp;
    string pstack;
    ifstream input;
    ofstream output;
    input.open("input.txt");
    output.open("output.txt");
    input>>t;
    for(i=1;i<=t+1;i++)
    {
        if(i==1){getline(input,pstack);continue;}
        getline(input,pstack);count=0;end_plus=0;  
	while(1)
        {
            beg_minus=0;count1=0;
            if(end_plus==0)
            {
                for(j=pstack.size()-1;j>=0;j--)
                {
                    if(pstack[j]=='+')
                        {count1++;}
                    else
                        break;
                }
                end_plus+=count1;
            }
            if(end_plus==pstack.size()){output<<"Case #"<<i-1<<": "<<count<<endl;break;}
            if(pstack[0]=='+')
            {
                for(j=1;j<pstack.size();j++)
                    {
                        if(pstack[j]=='+')continue;
                        else {j--;break;}
                    }
                count++;
                for(j1=0;j1<=j;j1++)
                {
                    pstack[j1]='-';
                }
                beg_minus=j+1;
               for(j1=j+1;j1<pstack.size();j1++)
		if(pstack[j1]=='-')beg_minus++;
                else break; 
	       //cout<<pstack<<" with "<<end_plus<<" and "<<beg_minus<<endl;
            }
	     else
            {
                   for(j=0;j<pstack.size();j++)
                    {
                        if(pstack[j]=='-')
                            beg_minus++;
                        else
                            break;
                    }
            }
	    count++;j1=pstack.size()-end_plus-1;
            if(beg_minus+end_plus==pstack.size()){count;output<<"Case #"<<i-1<<": "<<count<<endl;break;}
	     for(j=0;j<=j1/2;j++)
            {
                     if(pstack[j]=='+')temp='-'; else temp='+';
                     if(pstack[j1-j]=='+')pstack[j]='-';else pstack[j]='+';
                     pstack[j1-j]=temp;
            }
            end_plus+=beg_minus;
            if(end_plus==pstack.size()){output<<"Case #"<<i-1<<": "<<count<<endl;break;}
        }
    }
}





















