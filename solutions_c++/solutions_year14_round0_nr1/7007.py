#include<iostream>
#include<fstream>
#include<sstream>
using namespace std;
ofstream myfile("solution.txt");
int compare(int *val1,int *val2)
{
    int ctr=0;
    static int res;
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(*(val1+i)==*(val2+j))
            {
                ctr++;
                res=*(val1+i);
//                cout<<res;
            }
        }
        //cout<<"*val+1= "<<*(val1+i)<<"\n";
        if(ctr>1){
        myfile<<"Bad magician!";
        return 0;
        break;
        }
    }
    if(ctr==0){
        myfile<<"Volunteer cheated!";
        return 0;
    }
    else if(ctr==1)
    {
        myfile<<res;
        return res;
    }
}
int main()
{
    ifstream afile("A-small-attempt5.in",ios::in);
    char a,c[10];
    bool check=false;
    int b,i=0,val1[4],val2[4],limit=0,row;
    string sample;
    getline(afile,sample);
    stringstream conv;
    conv<<sample;
    conv>>limit;
    //cout<<limit;
    while(!afile.eof())
    {
        getline(afile,sample);
        conv.str("");
        conv.clear();
        conv<<sample;
        //cout<<"i= "<<i<<endl;
        //cout<<sample;
        //cout<<"i= "<<i<<endl;
        if(i%5==0)
        {
            conv>>row;
            cout<<"b= "<<row<<"\n";
            check=!(check);
        }
        else if((i%5)==row)
        {
            for(int j=0;j<4;j++)
            {

            conv>>b;
            if(check)
            {
                val1[j]=b;
                if(i<100)
                cout<<b<<" val1= "<<val1[j]<<endl;
            }
            else
            {
                val2[j]=b;
                if(i<100)
                cout<<b<<" val2= "<<val2[j]<<endl;
            }
           // cout<<b<<"\t";
            }
        }
        if(i>9 && i%10==0)
        {
            //int res=compare(val1,val2);
            myfile<<"Case #"<<i/10<<": ";
            int res=compare(val1,val2);
            //cout<<"res= "<<res<<endl;
            myfile<<endl;
        }
        i++;
        if((i%5)==limit)
        {
            //cout<<endl<<i;
            break;
        }
    }




        afile.seekg(2L,ios::cur);

    afile.close();
    return 0;
}
