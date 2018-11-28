#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
using namespace std;
int function(string &start,int length, int len_str, int len_ana){
	int answer=0;
	for(int i=0;i+len_ana<=len_str;i++){
		int number=0;
		for(int k=0;k<len_ana;k++){
			if(start[i+k]=='a'||start[i+k]=='u'||start[i+k]=='o'||start[i+k]=='i'||start[i+k]=='e')
				number=0;
			else number++;
			if(number==length)
				break;
		}
		if(number==length)
			answer++;
	}
	return answer;

}

void main(){

	
  fstream myfile ("inpu.txt",ios::binary|ios::in);
  fstream myfile1 ("out.txt",ios::trunc|ios::out);
  if (myfile.is_open())
  {
   
	  int number;
	  myfile>>number;
	  //cout<<number<<endl;
	  for (int i=0;i<number;i++){
		  string name;
		  int length;
		  myfile>>name;
		  myfile>>length;
		  int len_str=name.length();
		  int ans=0;
		  for(int i=len_str;i>=length;i--){
		  ans=ans+function(name,length,len_str,i);
		  }
		 
		  myfile1<<"Case #"<<i+1<<": "<<ans<<endl;
	  }
	  myfile1.close();
    myfile.close();
  }
  system("pause");
}