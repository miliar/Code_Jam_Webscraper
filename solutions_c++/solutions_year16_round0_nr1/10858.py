#include <iostream>

#include <fstream>



using namespace std;



ofstream myfile;

bool a[10];



bool check(int y,int n)
{
	//cout<<y<<" case: "<<n<<"\n";
	while(y!=0)
	{
		a[y%10]=true;
		y/=10;
	}

	for(int i=0; i<10;i++)
	{	
		if(a[i]==false)
			return false;
	}
	
	return true;
}



void zero()
{

	for(int i=0; i<10;i++)
	{
		a[i]=false;
	}

}



void test(int y, int n)
{
    bool tmp = false;
    for(int i=1; i<=100;i++)
    {
        if(check(y*i,n) )
        {
        	tmp = true;
        	y= y*i;
        	break;
		}

 	}
 	if(y==0 || tmp==false )
 		myfile << "Case #" << n <<": "<<"INSOMNIA"<<"\n";
 		
 	else
    	myfile << "Case #" << n <<": "<<y<<"\n";

}



void rea()
{

    ifstream read("input.txt");
    int lines,y;
    read>>lines;//number of lines

    for(int i=1;i<=lines;i++)
    {
            read>>y;
            zero();
            test(y,i);
    }
}



int main () 
{
    myfile.open ("output.txt");
    rea();
    myfile.close();
    return 0;
}
