#include <bits/stdc++.h>
using namespace std;

int f(string s, int k){
	int i,count,len,j;
	len=s.size();
	i=0;
	count=0;
	for(i=0;i<len;i++){
        cout<<i<<endl;
		if(s[i]=='-'){
			if(i+k>len){
				return -1;
			}
			else{
				for(j=i;j<i+k;j++){

					s[j]=(s[j]=='-' ?'+':'-');

				}
				count++;
			}
		}

	}
	return count;
}
int main(int argc, char const *argv[]){
	int t,n,i=0;
	string temp, temp1, temp2;

	fstream fin,fout;

	fin.open("input.in",ios::in);
	fout.open("output.txt",ios::out);
	fin>>temp;

	stringstream convert(temp);
	convert>>t;
	while(i<t){
		int k;
		fin>>temp1>>temp2;
		string str=temp1;
		stringstream convert(temp2);
		convert>>k;
		cout<<str<<endl<<k<<endl;
		int ans=f(str, k);
		if(ans<0){
            fout<<"Case #"<<i+1<<": IMPOSSIBLE\n";}

		else
            fout<<"Case #"<<i+1<<": "<<ans<<endl;
		i++;
	}
	return 0;
}
