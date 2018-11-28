#include <iostream>
#include<string>
#include<fstream>
using namespace std;

int main() 
{
	ifstream input("A-small-attempt6.in");
    ofstream output("A-small-attempt6_out.txt");
		int t,len,i,j;
	long int ans,people;
	string shy; // shyness string
	input>>t;
	for(j=0;j<t;j++)
	{
	    ans=0;
	   
	    input>>len;
	    input>>shy;
	    people=shy[0]-'0';
	    //cout<<"People :"<<people<<endl;
	        
	    //cout<<" len and shy"<<len <<" and"<<shy<<endl;
	    for(i=1;i<=len;i++)
	    {
	        if(shy[i]!='0')
	        {
	        //cout<<"People :"<<people<<endl;
	        if(i>people)
	        {
	            ans+=i-people;
	            //cout<<"ans :"<<ans<<endl;
	            people+=ans;
	        }
	        people+=(shy[i]-'0');
	        }
	    }
	    output<<"Case #"<<j+1<<": "<<ans<<endl;
	}
	return 0;
}
