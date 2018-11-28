#include <iostream>
#include <set>
#include <fstream>
using namespace std;

void one_trick(int case_no,ofstream& fout){
	int first_ans = 0, second_ans = 0;
	set<int> first_row,second_row,intersection;

	cin>>first_ans;
	for(int i=0;i<4;i++){
		int a=0,b=0,c=0,d=0;
		cin>>a>>b>>c>>d;
		
		if(i==first_ans-1){
			first_row.insert(a);
			first_row.insert(b);
			first_row.insert(c);
			first_row.insert(d);
		}
	}
	
	cin>>second_ans;
	for(int i=0;i<4;i++){
		int a=0,b=0,c=0,d=0;
		cin>>a>>b>>c>>d;
		
		if(i==second_ans-1){
			second_row.insert(a);
			second_row.insert(b);
			second_row.insert(c);
			second_row.insert(d);
		}
	}
	
	set_intersection(first_row.begin(),first_row.end(),second_row.begin(),second_row.end(),inserter(intersection,intersection.end()));
	
	set<int>::iterator it;
	//for(it=intersection.begin();it!=intersection.end();it++){
	//}
	
	fout<<"Case #"<<case_no<<": ";
	
	if(intersection.size()>1){
		fout<<"Bad magician!"<<endl;
	}
	else if(intersection.size()==0){
		fout<<"Volunteer cheated!"<<endl;
	}
	else{
		it=intersection.begin();
		fout<<*it<<endl;
	}
	
}

int main(){
	int tests = 0;
	cin>>tests;
	ofstream fout;
	fout.open("gcj_q1.out");
	
	for(int i=0;i<tests;i++){
		one_trick(i+1,fout);
	}
}