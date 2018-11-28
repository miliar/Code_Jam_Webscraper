#include <bits/stdc++.h>
using namespace std;

vector <string> magicstring;

void generator(string s,int l,int n)
{
	if(l>n) { magicstring.push_back(s); return;}
	//if(!filter(s)) return;
	generator(s+'1',l+1,n);
	generator(s+'0',l+1,n);
}
vector <string> magic;
void filter()
{  int flag = 1;
   int l = magicstring.size();
   for(int i=0;i<l;i++)
   {   string str = magicstring[i];
	   flag = 1;
	   int count1 =0;
	   for(int j=0;j<12;j++)
	   {   
		   if(str[j]=='1') count1++;
		   if(str[j]=='0') { if(count1%2) {flag=0;break;}
			                 count1=0; }
	   }
	   if(count1%2) flag=0;
	   if(flag) magic.push_back(str);
	   if(magic.size()==51) break;
   }
}

int main()
{
	//freopen("output1l.txt","w",stdout);
	generator("",0,11);
	filter();
	/*cout << magic.size() << endl;
	for(unsigned int i=0;i<magic.size();i++) cout << magic[i] << endl;*/
	string s,ss;
	int count = 0;
	int t; cin >> t;
	while(t--)
	{   int n,j;
		cin >> n >> j;
		printf("Case #1:\n");
		for(int i=0;i<50;i++)
		{
			for(int k = i+1;k<50;k++)
			{ count++;
			s = "11";
			ss = "11";
			s = s+magic[i];
			ss = ss + magic[k];
			s = s + "11";
			ss = ss + "11";
			s = s + ss;
			printf("%s ",s.c_str());
			for(int j=3;j<=11;j++) printf("%d ",j);
			printf("\n");
			if(count==500) return 0;
		   }
	    }
    }
    return 0;
}
