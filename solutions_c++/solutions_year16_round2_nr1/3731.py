#include <algorithm>

#include <iostream>
#include <fstream>

#include <string.h>
#include <limits>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <vector>
#include <list>
#include <set>
#include <set>
#include <sstream>
#include <stack>
#include <queue>

using namespace std;

ofstream myfile("output.in");

int findDigit(multimap<char,bool> alphabets,stack<string> number,int case_i){

    string numberstring[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
    bool found = false;

    bool full = true;
    for (multimap<char,bool>::iterator it=alphabets.begin(); it!=alphabets.end(); ++it)
    {
   // cout<<it->second<<" ";
        if(it->second == 0){
            full = false;
        }
    }

    if(full){
      //  cout<<"full"<<endl;
        int digits_arr[5000],i=0;

        while(!number.empty()){
            string num = number.top();
            number.pop();

//        cout<<num<<endl;
            if(num == "ZERO"){
                digits_arr[i++] = 0;
            }else if(num == "ONE"){
                digits_arr[i++] = 1;
            }
            else if(num == "TWO"){
                digits_arr[i++] = 2;
            }
            else if(num == "THREE"){
                digits_arr[i++] = 3;
            }
            else if(num == "FOUR"){
                digits_arr[i++] = 4;
            }
            else if(num == "FIVE"){
                digits_arr[i++] = 5;
            }
            else if(num == "SIX"){
                digits_arr[i++] = 6;
            }
            else if(num == "SEVEN"){
                digits_arr[i++] = 7;
            }
            else if(num == "EIGHT"){
                digits_arr[i++] = 8;
            }
            else if(num == "NINE"){
                digits_arr[i++] = 9;
            }
        }

        sort(digits_arr,digits_arr+i);

        cout<<"Case #"<<case_i<<": ";
        myfile<<"Case #"<<case_i<<": ";

        for(int j = 0 ; j < i; j++)
        {
            cout<<digits_arr[j];
            myfile<<digits_arr[j];
        }

        cout<<endl;
        myfile<<endl;

        return 1;
    }

    for(int i = 0; i<10 ;i++){
            bool availability = true;

            for(int j=0 ; j<numberstring[i].length() ; j++){
                char character = tolower(numberstring[i][j]);

                pair <std::multimap<char,bool>::iterator, multimap<char,bool>::iterator> ret;
                ret = alphabets.equal_range(character);

                bool foundpair = false;
                for (std::multimap<char,bool>::iterator it=ret.first; it!=ret.second; ++it){
                    if(it->second == 0){
                        foundpair = true;
                        break;
                    }
                }

                if(!foundpair){
                    availability = false;
                }
            }

            if(availability){
                found = true;
         //       cout<<"availability{"<<endl;
                number.push(numberstring[i]);

              //  cout<<numberstring[i]<<endl;
                for(int j=0 ; j<numberstring[i].length() ; j++){

                    char character = tolower(numberstring[i][j]);
                    pair <std::multimap<char,bool>::iterator, multimap<char,bool>::iterator> ret;
                    ret = alphabets.equal_range(character);

                    bool foundpair = false;
                    for (std::multimap<char,bool>::iterator it=ret.first; it!=ret.second; ++it){
                        if(it->second == 0){
                            it->second = 1;
                            break;
                        }
                    }
                }

                int value = findDigit(alphabets,number,case_i);
                if(value == 1) return 1;

                number.pop();
                for(int j=0 ; j<numberstring[i].length() ; j++){

                    char character = tolower(numberstring[i][j]);
                    pair <std::multimap<char,bool>::iterator, multimap<char,bool>::iterator> ret;
                    ret = alphabets.equal_range(character);

                    bool foundpair = false;
                    for (std::multimap<char,bool>::iterator it=ret.first; it!=ret.second; ++it){
                        if(it->second == 1){
                            it->second = 0;
                            break;
                        }
                    }
                }
           //     cout<<"availability}"<<endl;
            }
    }

    if(!found){
        return 0;
    }

    return 0;
}

int main(){

    int T;
    cin>>T;

    for(int case_i = 1 ; case_i<=T ; case_i++){

        string digits;
        cin>>digits;

        multimap<char,bool> alphabets;
        stack<string> number;

        for(int index = 0; index<digits.length();index++)
        {
            alphabets.insert(pair<char,bool>(tolower(digits[index]),false));
        }

        findDigit(alphabets,number,case_i);
   	}

    return 0;
}










