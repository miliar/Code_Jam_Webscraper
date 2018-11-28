#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#include<sstream>
#include<string>
#include<algorithm>
#include<unordered_map>

using namespace std;

void print_result(int i, string result)
{
	if (i != 1)
		cout << endl;
	cout<<"Case #"<< i<< ": ";
	cout << result;
}


string judgeLawn(vector<vector<int> > l){
	//find max in each row
	//m[col]=x
	//in the end compare col
	unordered_map<int, int> m;
	if(l.size()==1||l.size()==0)
		return "YES";
	for(int c=0; c<l.size(); c++){
		int max=0;
		//each row, first run
		for(int r=0; r<l[0].size(); r++){
			if(l[c][r]>max){
			  max=l[c][r];
			}
		}   
		//row, second run
		for(int r=0; r<l[0].size(); r++){
			if(l[c][r]<max){
				if(m.find(r)==m.end()){//didnt find
				   m[r]=l[c][r];
				} else{
				   if(m[r]!=l[c][r])
					   return "NO";
				}
			}
		}
	}

	//loop map
	for(unordered_map<int, int>::iterator it=m.begin(); it!=m.end(); it++){
	  int row = it->first;
	  int number = l[0][row];
	  //each row
	  for(int j=1; j<l.size(); j++){
	     if(l[j][row]!=number){
			 return "NO";
		 }
	  }
	}
	return "YES";
}


void main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int num_case;
	string str;
	string result;
    cin>>num_case;

	for(int i=1; i <= num_case; i++)
		{ 
	        getline(cin,str); //get to the second line 
			int rows, cols;
			cin>>rows;
			cin>>cols;
	        vector<vector<int> > lawn; 
			for(int j=0; j<rows; j++){
	          getline(cin,str);// get to the next line
			  vector<int> line;
			  for(int k=0; k<cols; k++){
			    int number;
				cin>>number;
				line.push_back(number);
			  }
			  lawn.push_back(line);
			}
			result = judgeLawn(lawn);
            print_result(i, result);

		}
	fclose (stdin);
	fclose (stdout);
}



