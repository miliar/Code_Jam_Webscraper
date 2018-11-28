#include <bits/stdc++.h>
#define NO_OF_CHARS 256
using namespace std;
void fillCharCounts(char *str, int *count){
   int i;
   for (i = 0; *(str+i);  i++)
      count[*(str+i)]++;
 
}


int main() {
	// your code goes here
	ios_base::sync_with_stdio(0);
	int t,i,j=1,s;
	ifstream infile;
	ofstream outfile;
	infile.open("A-large.in");
	outfile.open("output.txt");
	infile>>t;
	while(t--){
		s=0;
		vector<int> v;
	char str[2000];
	infile>>str;
	
	int *count = (int *)calloc(NO_OF_CHARS, sizeof(int));
    fillCharCounts(str, count);
	
		if(count['Z']>0){
			for(i=0;i<count['Z'];i++)
			v.push_back(0);
			
			count['E']-=count['Z'];
			count['R']-=count['Z'];
			count['O']-=count['Z'];
			count['Z']-=count['Z'];
		}
		
		if(count['G']>0){
			for(i=0;i<count['G'];i++)
			v.push_back(8);
			count['I']-=count['G'];
			count['E']-=count['G'];
			
			count['H']-=count['G'];
			count['T']-=count['G'];
			count['G']-=count['G'];
			
		}
		if(count['X']>0){
			for(i=0;i<count['X'];i++)
			v.push_back(6);
			count['S']-=count['X'];
			count['I']-=count['X'];
			count['X']-=count['X'];
			
		
		}
		if(count['W']>0){
			for(i=0;i<count['W'];i++)
			v.push_back(2);
			count['T']-=count['W'];
			
			count['O']-=count['W'];
			count['W']=0;
		}
		if(count['T']>0){
			for(i=0;i<count['T'];i++)
			v.push_back(3);
			
			count['E']-=2*count['T'];
			count['H']-=count['T'];
			count['R']-=count['T'];
			count['T']=0;
	
		}
		if(count['R']>0){
			for(i=0;i<count['R'];i++)
			v.push_back(4);
			count['F']-=count['R'];
			count['U']-=count['R'];
			
			count['O']-=count['R'];
			count['R']=0;
		}
		if(count['F']>0){
			for(i=0;i<count['F'];i++)
			v.push_back(5);
			
			count['E']-=count['F'];
			count['V']-=count['F'];
			count['I']-=count['F'];
			count['F']=0;
		}
		if(count['O']>0){
			for(i=0;i<count['O'];i++)
			v.push_back(1);
			count['N']-=count['O'];
			count['E']-=count['O'];
			count['O']=0;
			
		}
		
		
		if(count['V']>0){
			for(i=0;i<count['V'];i++)
			v.push_back(7);
			count['S']-=count['V'];
			count['E']-=2*count['V'];
			
			count['N']-=count['V'];
			count['V']=0;
	
		}
		if(count['I']>0){
			for(i=0;i<count['I'];i++)
			v.push_back(9);
			count['N']-=2*count['I'];
			count['E']-=count['I'];
			count['I']=0;
		
		}
	sort(v.begin(),v.end());
	
	outfile<<"Case #"<<j<<": ";
	for(i=0;i<v.size();i++)
	outfile<<v[i];
	outfile<<endl;
	j++;
	}
	return 0;
}
