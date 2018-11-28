#include <iostream>
#include<fstream>
#include<deque>
#include<algorithm>
#include<string.h>

using namespace std;
/*
struct Node
{
    Node* next;
};
*/
int main()
{
    /*fstream fin("input.txt",ios::in);
    fstream fout("output.txt",ios::out);
    int t;
    fin>>t;
    for(int z=1;z<=t;z++)
    {
        int l;
        int counter=0;
        fin>>l;
        Node *N[l] =  new Node[l];
        for(int i=0;i<l;i++){
            N[i]->next=NULL;
        }
        for(int i=0; i<l; i++)
        {
                int ch;
                fin>>ch;
                ch--;
                N[i]->next= N[ch];
        }
        for(int i=0;i<l;i++){
            Node* a;
            int mincount=0;
            a=N[i];
            do{
                a= N[i]->next;
                mincount++;
            }while(a!=NULL && a->next != N[i]);
            if(mincount>counter){
                counter=mincount;
            }
        }
        fout<<"Case #"<<z<<": "<<counter<<endl;
    }
    */


    int t;
    fstream fin("input.txt",ios::in);
    fstream fout("output.txt",ios::out);
    fin>>t;
    string crap;
    getline(fin,crap);
    for(int q=1;q<=t;q++)
    {
        string a;
        deque<int> d;
        getline(fin,a);
        d.push_back(a[0]);
        char ch=a[0];
        int counter=1;
        for(unsigned i=1; i<a.size(); i++)
        {
            if(ch > a[i] )
            {
                d.push_back(a[i]);
                counter++;

            }
            else if(ch<= a[i])
                {
                    d.push_front(a[i]);
                    counter++;
                    ch=a[i];
                }
        }
        fout<<"Case #"<<q<<": ";
        for(unsigned i=0;i<counter;i++){
            fout<<(char)d[i];
        }
        fout<<endl;
    }
    return 0;
}
