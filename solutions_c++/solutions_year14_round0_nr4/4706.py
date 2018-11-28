//============================================================================
// Author  	: Maciej Michalak
//============================================================================

#include <iostream>
#include <fstream>
#include <list>
using namespace std;

void sort(int left, int right, float *d){
  float piwot,x;
  int i, j;
  
  i = (left + right) / 2;
  piwot = d[i]; 
  d[i] = d[right];
  j = left;
  for (int i= left; i<right; i++){
    if (d[i] < piwot){
      x = d[i]; 
	  d[i] = d[j];
	  d[j] = x;
      j++;
  	}
  }
  d[right] = d[j]; 
  d[j] = piwot;
  if (left < j - 1)   sort(left, j - 1, d);
  if (j + 1 < right)  sort(j + 1, right, d);
}

int main() {
	
    ifstream f;
    ofstream ff;
    ff.open("test.out");
    f.open("test.in");
    
    int T;
    f>>T;

    for(int x=0; x<T; x++){
    	int N;
    	f>>N;
    	
    	float fff;
    	list<float> Naomi;
    	list<float> Ken;
    	Naomi.clear();
    	Ken.clear();
    	list<float> Naomi2;
    	list<float> Ken2;
    	Naomi2.clear();
    	Ken2.clear();
    	
    	for(int l=0; l<N; l++){
    		f>>fff;
    		Naomi2.push_front(fff);
    		Naomi.push_front(fff);
    	}
    	
    	for(int l=0; l<N; l++){
    		f>>fff;
    		Ken2.push_front(fff);
    		Ken.push_front(fff);
    	}
    
    	Ken.sort();
    	Naomi.sort();
    	Ken2.sort();
    	Naomi2.sort();
    	    	
    	int scoreWar=0;
    	int scoreWar2=0;
    	
    	for(list<float>::iterator i=Naomi.begin(); i!=Naomi.end(); i++){
    		list<float>::iterator j=Ken.begin();
    		while(*i>*j && j!=Ken.end()){
    			j++;
    		}
    		if(*i<*j){
    			Ken.remove(*j);
    		}
	    }
    	scoreWar = Ken.size();
    	
    	
    	
    	for(list<float>::iterator i=Naomi2.begin(); i!=Naomi2.end(); i++){
    		list<float>::iterator j=Ken2.begin();
    		if(*i>*j){
    			Ken2.remove(*j);
    		}
	    }
	    
   	 ff<<"Case #"<<x+1<<": "<<N-Ken2.size()<<" "<< scoreWar<<endl;
	}
    return 0;
}



