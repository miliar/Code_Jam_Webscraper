#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

std::vector<std::string> split(std::string str,std::string pattern) {
 std::string::size_type pos;
 std::vector<std::string> result;
 str+=pattern;
 int strsize=str.size();

 for(int i=0; i<strsize; i++)
 {
	 pos=str.find(pattern,i);
	 if(pos<strsize)
	 {
		 std::string s=str.substr(i,pos-i);
		 result.push_back(s);
		 i=pos+pattern.size()-1;
	 }
 }
 return result;
}


int main() {
    int caseCount,firstRow,secondRow,loopCount,resultCount;
    string firstNumber,secondNumber,badNumber;
    string firstString,secondString,resultKey;
    vector<string> finalResult;
    cin>>caseCount;
    while(caseCount>0){
        map<string,int> myMap;
        cin>>firstRow;
        cin.ignore();
        for(loopCount=1;loopCount<=4;loopCount++){
            if(loopCount==firstRow){
                getline(cin,firstNumber);
            }else{
                getline(cin,badNumber);
            }
        }
        vector<string> splitResult = split(firstNumber," ");
        for(int i=0; i<splitResult.size(); i++) {
             firstString = splitResult[i];
             myMap[firstString]=0;
        }
        cin>>secondRow;
        cin.ignore();
        resultCount = 0;
        for(loopCount=1;loopCount<=4;loopCount++){
            if(secondRow==loopCount){
                getline(cin,secondNumber);
            }else{
                getline(cin,badNumber);
            }
        }
        splitResult = split(secondNumber," ");
        for(int i=0; i<splitResult.size(); i++) {
             if(myMap.count(splitResult[i])>0){
                resultKey = splitResult[i];
                resultCount++;
             }
        }
        if(1==resultCount){
            finalResult.push_back(resultKey);
        }else{
            if(resultCount<1){
                finalResult.push_back("Volunteer cheated!");
            }else {
                finalResult.push_back("Bad magician!");
            }
        }
        caseCount--;
    }
    cout<<finalResult.size()<<endl;
    for(int j=0; j<finalResult.size(); j++) {
        cout<<"Case #"<<j+1<<": "<<finalResult[j]<<endl;
    }
    getline(cin,badNumber);
    return 0;
}
