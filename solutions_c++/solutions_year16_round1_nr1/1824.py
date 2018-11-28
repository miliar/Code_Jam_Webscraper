#include <iostream>
using namespace std;
#include<string>
#include<list>
int main()
{
    string s;
    int t;
    cin>>t;
    char temp1;
    char temp2;
    int i;
    int j;
    for (j=1;j<=t;j++)
    {list<char> l;
        cin>>s;
        l.push_back(s[0]);
        temp1=s[0];
        //temp2=s[l.size()];
        for(i=1;i<s.length();i++)
        {
            if(s[i]>temp1)
            {
            l.push_back(s[i]);
            temp1=s[i];
            }
            else
            {
            l.push_front(s[i]);
            temp2=s[i];
            }
            
            
        }
        l.reverse();
        cout<<"Case #"<<j<<":"<< " ";
        list<char>::iterator p = l.begin();
        while(p != l.end()){
		cout << *p  ;
		p++;
	}
        cout << "\n" << endl;
        
    }
    return 0;
}
