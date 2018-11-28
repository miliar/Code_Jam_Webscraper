#include <bits/stdc++.h>
using namespace std;

vector<int> ans;
int req[10][26];
string dig[] = {"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
int arr[26];

bool isPossible(int i)
{
	for(int k=0;k<26;k++){
		if(arr[k]>=req[i][k]);
		else return false;
	}
	return true;
}

void use(int i){
	for(int k=0;k<26;k++){
		arr[k]-=req[i][k];
	}
}

bool allUsedUp(){
	for(int i=0;i<26;i++)
		if(arr[i]!=0)
			return false;
	return true;
}

void find();

bool tryVal(int i){
	if(isPossible(i))
	{
		use(i);
		find();
		ans.push_back(i);
		return true;
	}
	return false;
}

void find(){
	if(allUsedUp())
		return;

	if(tryVal(0))
		return;
	if(tryVal(6))
		return;
	if(tryVal(2))
		return;
	if(tryVal(7))
		return;
	if(tryVal(5))
		return;
	if(tryVal(4))
		return;
	if(tryVal(3))
		return;
	if(tryVal(8))
		return;
	if(tryVal(1))
		return;
	if(tryVal(9))
		return;
}


int main(){	
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int cc=1, t;
	memset(req,0,sizeof(0));
	for(int i=0;i<10;i++){
		for(int j=0;j<dig[i].length();j++)
			req[i][dig[i][j]-'A']++;
	}
	cin>>t;
	string s;
	while(t--){
		cout<<"Case #"<<cc++<<": ";
		ans.clear();
		memset(arr,0,sizeof(arr));
		cin>>s;
		for(int i=0;i<s.length();i++)
			arr[s[i]-'A']++;

		find();
		sort(ans.begin(),ans.end());
		for(int k=0,l=ans.size();k<l;k++)
		{
			cout<<ans[k];
		}
		cout<<endl;
	}

	return 0;
}