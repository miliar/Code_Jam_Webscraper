#include<iostream>
using namespace std;

/*void doFlip(string &s, int n)
{
	int top= 0;
	int btm= n;
	while(top<=btm)
	{
		swap(s[top],s[btm]);
		if(s[top]=='+')
			s[top]='-';
		else
			s[top]='+';
		if(top!=btm)
		{
			if(s[btm]=='+')
				s[btm]='-';
			else
				s[btm]='+';
		}
		top++;
		btm--;
	}
}*/
void doFlip(string &s)
{
	char ch= s[0];
	int i=0;
	while(i<s.length()&&s[i]==ch)
	{
		if(ch=='-')
			s[i]='+';
		else
			s[i]='-';
		i++;
	}
}

int getPos(string s,char ch)
{
	
	for(int i=1;i<s.length();i++)
		if(s[i]==ch)
			return i;
    return -1;
}

bool chk(string s)
{
	for(int i=0;i<s.length();i++)
		if(s[i]=='-')
			return 0;
	return 1;
}

int main()
{
	int t;
	string s;
    cin>>t;
    int cnt=1;
    int num=0;
    while(t--)
    {
    	cin>>s;
    	int num=0;
    	while(1)
    	{
    		char ch;
    		if(s[0]=='-')
    			ch='+';
    		else
    			ch='-';
	        int mrk= getPos(s,ch);

	        if(mrk==-1&&chk(s)==1)
	    		break;

	    	doFlip(s);
	    	num++;
	    	
    	}
		cout<<"Case #"<< cnt++<<": "<<num<<endl;
    	
    }

}