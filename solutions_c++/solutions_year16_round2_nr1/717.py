#include <bits/stdc++.h>
using namespace std;

char str[2003];
int cnt[256],freq[10];
int main() {
	int tt,t,n,i,j;
	cin >> tt;
	for(t=1;t<=tt;t++){
		cout<<"Case #"<<t<<": ";
		cin >> str;

		n=strlen(str);
		memset(freq,0,sizeof freq);
		memset(cnt,0,sizeof cnt);
		for(i=0;i<n;i++)
			cnt[str[i]]++;
    	freq[0]=cnt['Z'];
		cnt['E']-=cnt['Z'];
		cnt['R']-=cnt['Z'];
		cnt['O']-=cnt['Z'];
        cnt['Z']=0;

		freq[2]=cnt['W'];
		cnt['T']-=cnt['W'];
		cnt['O']-=cnt['W'];
        cnt['W']=0;

		freq[4]=cnt['U'];
		cnt['F']-=cnt['U'];
		cnt['O']-=cnt['U'];
		cnt['R']-=cnt['U'];
        cnt['U']=0;

		freq[5]=cnt['F'];
		cnt['I']-=cnt['F'];
		cnt['V']-=cnt['F'];
		cnt['E']-=cnt['F'];
        cnt['F']=0;

		freq[6]=cnt['X'];
		cnt['S']-=cnt['X'];
		cnt['I']-=cnt['X'];
        cnt['X']=0;

		freq[7]=cnt['V'];
		cnt['S']-=cnt['V'];
		cnt['E']-=cnt['V'];
		cnt['E']-=cnt['V'];
		cnt['N']-=cnt['V'];
        cnt['V']=0;

		freq[8]=cnt['G'];
		cnt['E']-=cnt['G'];
		cnt['I']-=cnt['G'];
		cnt['H']-=cnt['G'];
		cnt['T']-=cnt['G'];
        cnt['G']=0;

		freq[1]=cnt['O'];
		cnt['N']-=cnt['O'];
		cnt['E']-=cnt['O'];
        cnt['O']=0;

		freq[3]=cnt['T'];
		cnt['H']-=cnt['T'];
		cnt['R']-=cnt['T'];
		cnt['E']-=cnt['T'];
		cnt['E']-=cnt['T'];
        cnt['T']=0;

		freq[9]=cnt['I'];
		cnt['N']-=cnt['I'];
		cnt['N']-=cnt['I'];
		cnt['E']-=cnt['I'];
        cnt['I']=0;

		for(i='A';i<='Z';i++)
			assert(cnt[i]==0);

		for(i=0;i<10;i++)
			for(j=0;j<freq[i];j++)
				cout<<i;
		puts("");




	}
}
