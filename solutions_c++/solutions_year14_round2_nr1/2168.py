#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<string>

using namespace std;

int main(){
	int N,testCase = 1,numS = 0;
	
	cin>>N;
	while(testCase <= N){
		cin>>numS;
		//vector<String> tempL;
		/*for(int i = 0; i < numS; i++){
			cin>>temp;
			tempL.push_back(temp);
		}*/
		string temp,temp2;
		cin>>temp>>temp2;
		vector<int> a,b;
		vector<char> c,d;
		int count = 1;
		for(int i = 1; i < temp.size(); i++){
			//cout<<temp[i]<<" "<<temp[i-1]<<"\n";
			if(temp[i] != temp[i-1]) {
				//cout<<count<<"\n";
				a.push_back(count);
				c.push_back(temp[i-1]);
				//cout<<"size "<<a.size()<<"\n";
				count = 0;
			}
			count++;
		}
		//if(temp[temp.size()-1] != temp[temp.size()-2])
		//cout<<count<<"\n";
		a.push_back(count);
		c.push_back(temp[temp.size()-1]);
		//cout<<"size "<<a.size()<<"\n";
		//cout<<"\n";
		
		count = 1;
		for(int i = 1; i < temp2.size(); i++){
			if(temp2[i] != temp2[i-1]) {
				b.push_back(count);
				d.push_back(temp2[i-1]);
				count = 0;
			}
			count++;
		}
		b.push_back(count);
		d.push_back(temp2[temp2.size()-1]);
		int moves = 0;
		int no = 0;
		if(a.size() != b.size()) {
			printf("Case #%d: Fegla Won\n",testCase);
		}
		else{
			for(int i = 0; i < a.size(); i++){
				//cout<<" here "<<a[i]<<" "<<b[i]<<"\n";
				if(c[i] != d[i]) {
					//cout<<c[i]<<" "<<d[i]<<"\n";
					no = 1;
					break;
				}
				else{
					if(a[i] != b[i])
						moves += max(a[i],b[i]) - min(a[i],b[i]);
				}
			}
			if(no) 
				printf("Case #%d: Fegla Won\n",testCase);
			else 
				printf("Case #%d: %d\n",testCase,moves);
		}
		testCase++;
	}
	
}