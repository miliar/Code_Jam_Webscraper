#include<iostream>
#include<algorithm>
#include<fstream>


int flipped(char status[],int size){
	int i=0,j=1;
	int no=0;
	while(j<size){
	if(status[i]!=status[j])
		no++;
	i++;
	j++;
	}
	return no;
}


int flip_number(char status[],int size){
	using namespace std;
	if(status[0]==status[size-1] && status[0]=='+')
		return flipped(status,size);
	if(status[0]==status[size-1] && status[0]=='-')
		return flipped(status,size)+1;
	if(status[0]=='-' && status[size-1]=='+')
		return flipped(status,size);
	if(status[0]=='+' && status[size-1]=='-')
		return flipped(status,size)+1;
	return -1;
}


int main(void)
{
	using namespace std;
	ifstream ifile("input");
	ofstream ofile("output");
	int total_case;
	char ch[101];
	int size;
	ifile>>total_case;
	for(int i=1;i<=total_case;i++){
		ifile>>ch;
		for(size=0;ch[size]!='\0';size++);
		ofile<<"Case #"<<i<<": "<<flip_number(ch,size)<<endl;
	}
	/* char ch[100]; */
	/* cin>>ch; */
	/* cout<<endl; */
	/* int size; */
	/* for(size=0;ch[size]!='\0';size++); */
	/* cout<<flip_number(ch,size)<<endl; */
	return 0;
}
