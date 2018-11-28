#include<cstdio>
#include<vector>
#include<map>
#include<math.h>
#include<algorithm>
using namespace std;

vector<int> ans;
char ch[2004];
int ar[26];
int main()
{
int ntc; scanf("%d",&ntc);
	for(int tc=1;tc<=ntc;tc++)
	{
		printf("Case #%d: ",tc);
		scanf("%s",&ch);
		
		for(int i=0;i<26;i++) ar[i] = 0;
		ans.clear();
		
		for(int i=0;ch[i]!='\0';i++)
		{
			
			ar[ch[i]-'A']++;
		}
		
		//printf("ch is %s\n",ch);
		while(ar['Z'-'A'])
		{
			ans.push_back(0);
			ar['Z'-'A'] --;
			ar['E'-'A']--;
			ar['R'- 'A']--;
			ar['O'- 'A']--;
			
		}
		while(ar['W' - 'A'])
		{
			ans.push_back(2);
			ar['T'-'A'] --;
			ar['W'-'A']--;
			ar['O'- 'A']--;
		}
		
		while(ar['X' - 'A'])
		{
			ans.push_back(6);
			ar['S'-'A'] --;
			ar['I'-'A']--;
			ar['X'- 'A']--;
		}
		while(ar['G' - 'A'])
		{
			ans.push_back(8);
			ar['E'-'A'] --;
			ar['I'-'A']--;
			ar['G'- 'A']--;
			ar['H'-'A']--;
			ar['T'- 'A']--;
		}
		
		while(ar['U' - 'A'])
		{
			ans.push_back(4);
			ar['F'-'A'] --;
			ar['O'-'A']--;
			ar['U'- 'A']--;
			ar['R'-'A']--;
		}
		
		while(ar['S' - 'A'])
		{
			ans.push_back(7);
			ar['S'-'A'] --;
			ar['E'-'A']--;
			ar['V'- 'A']--;
			ar['E'-'A']--;
			ar['N'-'A']--;
		}
		
		
		while(ar['T' - 'A'])
		{
			ans.push_back(3);
			ar['T'-'A'] --;
			ar['H'-'A']--;
			ar['R'- 'A']--;
			ar['E'-'A']--;
			ar['E'-'A']--;
		}
		
		
			while(ar['O' - 'A'])
		{
			ans.push_back(1);
			ar['O'-'A'] --;
			ar['N'-'A']--;
			ar['E'- 'A']--;

		}
		
			while(ar['F' - 'A'])
		{
			ans.push_back(5);
			ar['F'-'A'] --;
			ar['I'-'A']--;
			ar['V'- 'A']--;
			ar['E'-'A']--;
	
		}
		
		while(ar['N' - 'A'])
		{
			ans.push_back(9);
			ar['N'-'A'] --;
			ar['I'-'A']--;
			ar['N'- 'A']--;
			ar['E'-'A']--;
	
		}
		
		sort(ans.begin(),ans.end());
		
		for(int i=0;i<ans.size();i++) printf("%d",ans[i]);
		printf("\n");
	}	
}

