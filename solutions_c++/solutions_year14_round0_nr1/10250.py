#include<iostream>
#include<sstream>
#include<fstream>

using namespace std;
int main()
 {
	int testcases;
	int row1;
	int row2;
	ifstream in("input.txt");
	ofstream out("output.txt");
	in>>testcases;
    for(int f=1;f<=testcases;f++){
        int arr[2][4];
        in>>row1;
        string a;
        getline(in,a);
        for(int e=1;e<row1;e++)
            getline(in,a);
        for(int e=0;e<4;e++)
            in>>arr[0][e];
        getline(in,a);
        for(int e=0;e<4-row1;e++)
            getline(in,a);
        in>>row2;
        for(int e=0;e<row2;e++)
            getline(in,a);
        for(int e=0;e<4;e++)
            in>>arr[1][e];
        getline(in,a);
        for(int e=0;e<4-row2;e++)
            getline(in,a);
        int temp,count=0;

        for(int i=0;i<4;i++)
            for (int j=0;j<4;j++)
            if(arr[0][i]==arr[1][j])
            {
                ++count;
                temp=arr[0][i];
            }
        if (count==0)
            out<<"Case #"<<f<<": Volunteer cheated!\n";
        if(count==1)
            out<<"Case #"<<f<<": "<<temp<<endl;
        if (count>1)
            out<<"Case #"<<f<<": Bad magician!\n";
}//end of caea
}
