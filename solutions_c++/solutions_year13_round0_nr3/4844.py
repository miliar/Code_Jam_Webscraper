#include <iostream>
#include <string>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <string.h>
#include <vector>
#include <stdlib.h>
using namespace std;

bool isOdd(int x){
    if(x % 2) return true;
    else return false;
}

bool checkPalin(int a){
    stringstream strs;
    strs << a;
    string temp_str = strs.str();
    char * char_type = (char *)temp_str.c_str();
    int length = strlen(char_type);

    int mean;
    if(isOdd(length)){
	mean = floor(length/2);
	for (int i = 0; i<= mean-1; i++){
	    char left = char_type[i];
	    char right = char_type[length-1-i];
	    if(left!=right) return false;
	}
    }else {
	mean = length/2;
	for(int i = 0; i<= mean-1; i++){
	    char left = char_type[i];
	    char right = char_type[length-1-i];
	    if(left!=right) return false;
	}
    }
    return true;
}


int reverseint(int num_){
        int inv; inv = 0;

        while (num_>0)
        {
                inv = inv * 10 + (num_%10);
                num_ = num_ / 10;
        }

        return inv;
}

vector<int> palinGenWithSize(int a, int b, int s){
    vector<int> instance;
    if(s == 1){
	for(int i=1; i<10; i++){
	    if(a<=i && i<=b) instance.push_back(i);
	}
    }else if(!isOdd(s)){
	int magic = s/2;
	string numStr;
	for(int i = 1; i<pow(10,magic); i++){
//	    cout << i << " " << reverseint(i) << endl;
	    stringstream temp1;
	    stringstream temp2;
	    temp1 << i;
	    temp2 << reverseint(i);
	    string left = temp1.str();
	    string right = temp2.str();
	    while(left.length() != right.length()){
		string temp = "0";
		temp.append(right);
		right = temp;
	    }
	    if(left.length() ==magic && magic == right.length()){
	        //cout << left << " " << right << endl;
		left.append(right);
//		cout << left << endl;
		int value = atoi(left.c_str());
		if(a<=value && value<= b){
		    instance.push_back(value);
		}
	    }
	}
	  
    }else if(isOdd(s)){

	int magic = (s-1)/2;
	string numStr;
	for(int i = 1; i<pow(10,magic); i++){
//	    cout << i << " " << reverseint(i) << endl;
	    stringstream temp1;
	    stringstream temp2;
	    temp1 << i;
	    temp2 << reverseint(i);
	    string left = temp1.str();
	    string right = temp2.str();
	    while(left.length() != right.length()){
		string temp = "0";
		temp.append(right);
		right = temp;
	    }
	    if(left.length() ==magic && magic == right.length()){
	        //cout << left << " " << right << endl;
		for(int k = 0; k<10; k++){
		    string saveLeft = left;
		    stringstream temp3;
		    temp3 << k;
		    string mid = temp3.str();
		    left.append(mid);
		    left.append(right);
//		    cout << left << endl;
		    int value = atoi(left.c_str());
		    if(a<=value && value<= b){
		        instance.push_back(value);
		    }
		    left = saveLeft;
		}
	    }
	}
	 
    } 

//cout << "size " << instance.size() << endl;
    return instance;
}


int square(int a){
    return pow(a, 2);
}

bool isInteger(float k){
    return floor(k) == k;
}

/*
vector<int> deleteNotSquare(vector<int> a){
    vector<int> instance;
    for(unsigned int i = 0; i<a.size(); i++){
	float k = sqrt(a[i]);
	if( isInteger(k) && checkPalin(k)){

cout << a[i] << " " << k << endl;
	    instance.push_back(a[i]);
	}
    }
    return instance;
}

vector<int> addIsSquare(vector<int> a, int t){
    vector<int> instance;
    for(unsigned int i = 0; i<a.size(); i++){
	int k = square(a[i]);
	if(checkPalin(k) && k> t){
	    instance.push_back(k);
	}
    }
    return instance;
}
*/
vector<int> filter(vector<int> a, int min, int max){
    vector<int> instance;
//cout << "filtermin " << min << " ";
//cout << "filtermax " << max << endl;
    for (int i = 0; i<a.size(); i++){
	float rk = sqrt(a[i]);
	int sk = square(a[i]);
	if(min<=a[i] && a[i]<=max && isInteger(rk) && checkPalin(rk) ){
//cout << "rrr" << a[i] << endl;
	    instance.push_back(a[i]);
	  
	}
	if( min<= sk && sk<=max  && checkPalin(sk) && sk!=1){	// min<=a[i] && a[i] << max
//cout << "sss" << a[i] << endl;
	    instance.push_back(sk);
	    
	}
    }
    return instance;
}

void print(string message, vector<int> a){
cout << message << " ";
for(int i = 0; i<a.size(); i++){
cout << a[i] << " ";
}
cout << endl;
}

vector<int> palinGen(int a, int b){
    vector<int> all;
//    for(int i = a; i < threshold+1; i++){

	stringstream strs;
	int b1 = floor(sqrt(b));
	int upperbound;
 	if(b1 < a) {
	    strs << a;
	    upperbound = a;
	}else{
	    strs << b1;
	    upperbound = b1;
	}
	string temp_str = strs.str();
	char * char_type = (char *)temp_str.c_str();
	int max = strlen(char_type);

	
	stringstream strs1;
	int a1 = floor(sqrt(a));
	strs1 << a1;
	string temp_str1 = strs1.str();
	char * char_type1 = (char *)temp_str1.c_str();
	int min = strlen(char_type1);

        
//cout << "min " <<  min  << " " << a1 << endl;
//cout << "max " << max << " " << upperbound <<endl;



	for(int j = min; j<=max; j++){
//cout << j << endl;
	    vector<int> instance = palinGenWithSize(sqrt(a), upperbound, j);
//print("pinstance", instance);
//	    vector<int> instance1 = deleteNotSquare(instance);
	    instance = filter(instance, a, b);
//cout << "minbound" << a << endl;
//cout << "upperbound" << upperbound << endl;

	    all.insert(all.end(), instance.begin(), instance.end());
//print("instance", instance);
//print("instance1", instance1);

//	    vector<int> instance2 = addIsSquare(instance, threshold);
//	    all.insert(all.end(), instance2.begin(), instance2.end());

//print("instance2", instance2);
	}

  //  }
    return all;

}

int runFairSquare(){
    double low, up;
    cin >> low;
    cin >> up;
    vector<int> instance = palinGen(low, up);
//cout << "low " << low << " up " << up << endl;
//print("numbers: ", instance);
    sort(instance.begin(), instance.end());
    instance.erase( unique( instance.begin(), instance.end()), instance.end());
//print("uniques: ", instance);	
    return instance.size();
}

int main(){
//    cout << "hello" << endl;
//    checkPalin(121);
//palinGenWithSize(1, 99999, 5);
//vector<int> instance = palinGenWithSize(10, 100, 2);
//vector<int> instance = palinGen(100, 1000);
//cout << instance.size() << endl;

	int caseNumber;
	cin >> caseNumber;
	for(int i = 0; i<caseNumber; i++){
	    cout << "Case #" << i+1 << ": " << runFairSquare() << endl;
	}
	    
/*
for(int i = 0; i<instance.size(); i++){
	cout << instance[i] << " ";
}
cout << endl;
*/
    return 0;
}
