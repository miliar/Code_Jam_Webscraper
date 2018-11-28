//============================================================================
// Name        : LawnMower.cpp
// Author      : Rahul Verma
// Version     : 1.0
// Copyright   : none
// Description : none
//============================================================================

#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;

class pattern{
public:
	int *rows;
	int *tempRows;
	int width,height;

    void prepareTemp(int i);
	void init(int _width,int _height);
	void print();
	void addRow(int y,string values);
	string getStatus();
};
void pattern::init(int _width,int _height){

	height=_height;
	width=_width;
	rows = new int[width*height];
    tempRows=new int[width*height];
}

void pattern::print(){
	cout<<endl;
	for(int y=0;y<height;y++){
		cout<<endl;
		for(int x=0;x<width;x++)
		cout<<" "<<rows[(y*width)+x];
	}
}


void pattern::addRow(int y,string values){
	int pos1=0,pos2;
	for(int x=0;x<width;x++){
		pos2=values.find(" ",pos1);
		stringstream t;
		t<<values.substr(pos1,pos2-pos1);
		t>>rows[(y*width)+x];
		tempRows[(y*width)+x]=rows[(y*width)+x];
		pos1=pos2+1;
	}

}

void pattern::prepareTemp(int i){
	for(int y=0;y<height;y++){
		for(int x=0;x<width;x++){
			if(tempRows[(y*width)+x]<i)
				tempRows[(y*width)+x]=i;
		}
	}
}

string pattern::getStatus(){
    int t;
	for(int e=1;e<101;e++){
    	if(e!=1)
    		prepareTemp(e);
	for(int y=0;y<height;y++){
        for(int x=0;x<width;x++){
        	t=tempRows[(y*width)+x];
        	if(t==e){
        		for(int z=0;z<width;z++){

        			if(tempRows[(y*width)+z]!=e){
        				for(int w=0;w<height;w++){
        					if(tempRows[(w*width)+x]!=e){
        						return "NO";
        					}
        				}
        			}

        		}
        	}
        }
    }

    }
    return "YES";
}

/*
string pattern::getStatus(){
	for(int y=0;y<height;y++){
		string yth=rows[y];
		for(int x=0;x<width;x++){
			char c=yth[x];
			if(c=='1'){
				for(int z=0;z<width;z++){
					if(yth[z]!='1'){
						for(int w=0;w<height;w++){
							if(rows[w][x]!='1')
								return "NO";
						}
					}
				}


			}


		}


	}



	return "YES";
}
*/

string replaceChar(string str, char ch1, char ch2) {
  string temp=str;
	for (int i = 0; i < str.length(); ++i) {
    if (str[i] == ch1)
      temp[i] = ch2;
  }

  return temp;
}


int main() {




	  ifstream in("a.in");
	  stringstream buffer;
	  buffer << in.rdbuf();
	  string test = buffer.str();

	  size_t pos1 = 0;
	  size_t pos2;

	  pos2=test.find('\n',0);
	  string num=test.substr(0,pos2);
      pos1 = pos2+1;
      stringstream ss;
	  ss<<num;
	  int T;
	  ss>>T;

	  pattern *patterns=new pattern[T];
	  for(int x= 0;x<T;x++){


	      pos2 = test.find("\n", pos1);

		  string sizeS=test.substr(pos1, (pos2-pos1));
		  int i=sizeS.find(" ", 0);
		  string heightS=sizeS.substr(0, i);
		  string widthS=sizeS.substr(i+1, sizeS.length()-i-1);
		  stringstream a,b;
		  a<<heightS;
		  b<<widthS;
		  int w,h;
		  a>>h;
		  b>>w;

		  cout<<endl<<"height="<<h<<"  width="<<w;
		  pos1 = pos2+1;
		  pattern temp;
		  temp.init(w,h);
		  patterns[x]=temp;
		  for(int i=0;i<h;i++){
			  pos2 = test.find("\n", pos1);
              string row=test.substr(pos1, (pos2-pos1));
              patterns[x].addRow(i,row);

              pos1 = pos2+1;
		  }




	  }


	  for(int i =0;i<T;i++){
		  cout<<endl<<endl<<"and the pattern is \n";
		  patterns[i].print();
	  }

	  ofstream myfile ("a.out");
	  	  if (myfile.is_open())
	  	  {
	  		for(int i=0;i<T;i++){
	  		myfile<<"Case #"<<i+1<<": "<<patterns[i].getStatus();
	  		if(i!=T-1)
	  			myfile<<'\n';
	  		}
	  	     myfile.close();
	  	  }
	  	  else cout << "Unable to open file";


		  cout<<endl<<endl<<"statuses";
		  for(int i=0;i<T;i++){
			  cout<<endl<<"Case #"<<i+1<<": "+patterns[i].getStatus();

		  }



/*
	  string *inputs=new string[4*T];

string temp;
       cout<<endl<<T;
	    for (int x=0,y=0; x<(T*4)+T; x++){

	        pos2 = test.find("\n", pos1);
	        //search for the bar "|". pos2 will be where the bar was found.

	        temp= test.substr(pos1, (pos2-pos1)); //make a substring, wich is nothing more
	        if(temp.length()==4)
	        {
	        inputs[y]=temp;
	        y++;
	        }
	        //than a copy of a fragment of the big string.
	        pos1 = pos2+1; // sets pos1 to the next character after pos2.
	                         //so, it can start searching the next bar |.
	    }






	string *results=new string[T];
	string inputToPass[4];
*
	for(int i=0;i<T;i++){
		for(int y=0;y<4;y++)
			inputToPass[y]=inputs[(4*i)+y];

		results[i]=getStatus(inputToPass);
        cout<<endl<<"Case #"<<i+1<<": "<<results[i];
	}

*/
return 0;
}

