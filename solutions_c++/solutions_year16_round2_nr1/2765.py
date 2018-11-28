#include<bits/stdc++.h>
using namespace std;

int main()
{
	FILE *fp1,*fp2;
	fp1 = fopen("A-large.in","r");
	fp2 = fopen("output.txt","w");
	int t;
	char s[2005];
	int a[30],p[15],c;
	fscanf(fp1,"%d",&t);
	for(int j=1;j<=t;j++){
		for(int i=0;i<30;i++)
		a[i] = 0;
		for(int i=0;i<10;i++)
		p[i] =0;
		fscanf(fp1,"%s",s);
		//cout<<s<<endl;
		for(int i=0;s[i]!='\0';i++){
			a[s[i]-65]++;
		}
		
		if(a['Z'-'A']>0){
			c = a['Z'-'A'] ;
			a['E'-'A'] -= c;
			a['R'-'A'] -= c;
			a['O'-'A'] -= c;
			a['Z'-'A'] = 0;
			p[0] += c;
		}
		if(a['W'-'A']>0){
			c = a['W'-'A'];
			a['T'-'A'] -= c;
			a['O'-'A'] -= c;
			a['W'-'A'] = 0;
			p[2] += c;
		}
		if(a['U'-'A']>0){
			 c = a['U'-'A'];
			a['F'-'A'] -= c;
			a['R'-'A'] -=c;
			a['O'-'A'] -= c;
			a['U'-'A'] = 0;
			p[4] += c;
		}
		if(a['X'-'A']>0){
			c = a['X'-'A'];
			a['I'-'A'] -= c;
			a['S'-'A'] -=c;
			a['X'-'A'] = 0;
			p[6] += c;
		}
		if(a['G'-'A']>0){
			c = a['G'-'A'];
			a['E'-'A'] -= c;
			a['I'-'A'] -=c;
			a['H'-'A'] -= c;
			a['T'-'A'] -= c;
			a['G'-'A'] = 0;
			p[8] += c;
		}
		if(a['O'-'A']>0){
			c = a['O'-'A'];
			a['E'-'A'] -= c;
			a['N'-'A'] -=c;
			a['O'-'A'] -= c;
			p[1] += c;
		}
		if(a['S'-'A']>0){
			c  = a['S'-'A'];
			a['E'-'A'] -= c;
			a['V'-'A'] -=c;
			a['E'-'A'] -= c;
			a['N'-'A'] -= c;
			a['S'-'A'] = 0;
			p[7] += c;
		}
		if(a['R'-'A']>0){
			c = a['R'-'A'];
			a['T'-'A'] -= c;
			a['H'-'A'] -=c;
			a['E'-'A'] -= c;
			a['E'-'A'] -= c;
			a['R'-'A'] = 0;
			p[3] += c;
		}
		if(a['F'-'A']>0){
			c = a['F'-'A'];
			a['I'-'A'] -= c;
			a['V'-'A'] -=c;
			a['E'-'A'] -= c;
			//a['T'-'A'] -= c;
			a['F'-'A'] = 0;
			p[5] += c;
		}
		if(a['E'-'A']>0){
			c = a['E'-'A'];
			a['N'-'A'] -= c;
			a['I'-'A'] -=c;
			a['N'-'A'] -= c;
			//a['T'-'A'] -= c;
			a['E'-'A'] = 0;
			p[9] += c;
		}
		fprintf(fp2,"Case #%d: ",j);
		for(int i=0;i<10;i++){
			while(p[i]){
				fprintf(fp2,"%d",i);
				p[i]--;
			}
		}
		fprintf(fp2,"\n");
	
		}
		fclose(fp1);
		fclose(fp2);
	return 0;
}
