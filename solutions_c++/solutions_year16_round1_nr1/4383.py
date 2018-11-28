#include <iostream>
#include<stdio.h>
using namespace std;


int main() {
    int len, t, i, j;
    string word, newword;
	
	cin >> t;
	
	for(j=0;j<t;j++){
	    cin >> word;
	    
	    len = word.length();
	    
	    newword = word[0];
	    
	    for(i=1;i<len;i++){
	        
	        if(word[i] < newword[0]){
	            newword = newword + word[i];
	        }
	        else{
	           // char temp[100];
	           // strcpy(newword, temp);
	           // newword[0] = word[i];
	           // for(j=1;j<i-1;j++){
	           //     newword[j] = temp[j-1];
	           // }
	           string temp = word[i] + newword;
	           newword = temp;
	           
	        }
	        
	    }
	    cout<<"Case #"<<j+1<<": "<<newword<<"\n";
	    
	   // printf("%s",newword);
	   //printf("%s",word);
	        
	    }
	
	
	return 0;
}

