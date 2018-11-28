#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

int num_digits( int a){

  if(a/10==0){
    return 1;
  }
  else {
    return 1+num_digits(a/10);
  }
}

vector<int> prod (vector<int> a, vector<int> b)
{
    vector<int> retval;
    retval.push_back(a.at(0)*b.at(0)- a.at(1)*b.at(1) - a.at(3)*b.at(3) - a.at(2)*b.at(2));
    retval.push_back(a.at(0)*b.at(1)+ a.at(1)*b.at(0) - a.at(3)*b.at(2) + a.at(2)*b.at(3));
    retval.push_back(a.at(0)*b.at(2)- a.at(1)*b.at(3) + a.at(2)*b.at(0) + a.at(3)*b.at(1));
    retval.push_back(a.at(0)*b.at(3)+ a.at(1)*b.at(2) - a.at(2)*b.at(1) + a.at(3)*b.at(0));

    return retval;
}

vector<int> product (vector <int> a, char b)
{

  int x []={0,1,0,0}, y [] = {0,0,1,0}, z []={0,0,0,1};
  vector<int> i (x, x + sizeof(x)/sizeof(int) );
  vector<int> j (y, y + sizeof(y)/sizeof(int) );
  vector<int> k (z, z + sizeof(z)/sizeof(int));

  if(b=='i'){
    return prod(a,i);
  }

  if(b=='j'){
    return prod(a,j);
  }

  return prod(a,k);

}

int main ()
{
  int x []={0,1,0,0}, y [] = {0,0,1,0}, z []={0,0,0,1}, w1 []={1,0,0,0};
  vector<int> i (x, x + sizeof(x)/sizeof(int) );
  vector<int> j (y, y + sizeof(y)/sizeof(int) );
  vector<int> k (z, z + sizeof(z)/sizeof(int));
  vector<int> w (w1, w1 + sizeof(w1)/sizeof(int) );








/* string line;
  ifstream myfile ("abc.txt");
  if (myfile.is_open())
  {
    string::size_type sz; int i;

    while ( getline (myfile,line) )
    {
      //cout << line << endl;
        i=stoi (line, &sz);
        cout<<i<<endl;
        line.erase(0,num_digits(i)+1);
        i=stoi (line, &sz);
        cout<<i<<endl;
    }
    myfile.close();
  }

  else cout << "Unable to open file"; 

  */




  string line;
  string result[100];

  ifstream myfile ("C-small-attempt1.in");
  if (myfile.is_open())
  {
    string::size_type sz;
    getline (myfile,line);
    {

      int num_test = stoi(line, &sz);


      for(int m=0; m<num_test; m++){
        getline(myfile, line);
        int L= stoi(line, &sz);
        line.erase(0,num_digits(L)+1);
        int X= stoi(line, &sz);
        getline(myfile,line);
        string characters=line;

  // first append and make the string

    for(int n=0; n<X-1;n++){
        for(int o=0; o<L;o++){
            characters.push_back(characters.at(o));
        }
    }

  vector<int> mult (w);
  bool i_found= false, j_found=false, k_found=false;

  //for loop of string size. keep selecting each char one by one. start by product of w vector and char.at(0)
  for(int p=0; p<X*L; p++){
    mult= product(mult, characters.at(p));
    if(mult==i && !i_found){
      i_found=true;
      mult=w;
    }

    if(i_found && !j_found && mult==j){
        j_found=true;
        mult=w;
    }

    if(j_found && !k_found && mult==k)
    {
      k_found=true;
      mult=w;
    }
  }


  if(k_found && mult==w)
  {
    //cout<<"Case #"<<m+1<<": YES"<<endl;
    result[m]="YES";
  }

  else{
    //cout<<"Case #"<<m+1<<": NO"<<endl;
    result[m]="NO";
  }

  //have three bool i_found, j_found, k_found. when i_found is false and product is vector i, then make i_found true and product variable w vector.
  //within if i_found, do same for j
  // then under condition that i_found and j_found do same for k
  // lstly, out of for loop if k_found and product equals w then YES ELSE NO

  }

  for(int blah=0; blah<num_test; blah++)
  {
    cout<<"Case #"<<blah+1<<": "<<result[blah]<<endl;

  }

  }
        myfile.close();
      }

  return 0;
}
