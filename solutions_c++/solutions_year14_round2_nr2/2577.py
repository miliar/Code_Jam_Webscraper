#include<iostream>
using namespace std;
class a{
public:
a(){cout<<'a';}


};
class b{
public:
b(){cout<<'b';}


};
class c{
    b bs;
    a as;

public:
c(){cout<<'c';}


};

int main(){
c c;

}



