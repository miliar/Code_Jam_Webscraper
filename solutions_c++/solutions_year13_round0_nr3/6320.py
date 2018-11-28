#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#include<sstream>
#include<string>
#include<algorithm>


using namespace std;

void print_result(int i, int result)
{
	if (i != 1)
		cout << endl;
	cout<<"Case #"<< i<< ": ";
	cout << result;
}

bool isPalind(int num){
	stringstream ss;
    ss << num;
    string str = ss.str();
	int p1=0;
	int p2= str.length()-1;
	while(p1<p2){
	  if(str[p1]!=str[p2])
		  return false;
	  p1++;
	  p2--;
	}
	return true;
}

int getNumber(int p_min, int p_max){
	int count=0;
	int min= ceil(sqrt(p_min+0.0));
	int max= floor(sqrt(p_max+0.0));
	for(int i= min; i<=max; i++){
		if(isPalind(i)){
		  if(isPalind(i*i))
			  count++;
		}
	}
	return count;
}


void main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int num_case;
	string str;
    cin>>num_case;

	for(int i=1; i <= num_case; i++)
		{ 
	        getline(cin,str); //get to the second line 
	        int min, max;
            cin>>min;
			cin>>max;
			int result = getNumber(min, max);
            print_result(i, result);

		}
	fclose (stdin);
	fclose (stdout);
}




