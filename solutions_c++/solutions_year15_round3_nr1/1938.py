#include<iostream>
#include<fstream>
#include<string>

int main()
{
std::streambuf *coutbuf = std::cout.rdbuf();
std::streambuf *cinbuf = std::cin.rdbuf();

std::ofstream out("outputfile1.out");
std::ifstream in("A-small-attempt1.in");

std::cin.rdbuf(in.rdbuf());

std::cout.rdbuf(out.rdbuf());

int nTestCases,n;
std::cin>>nTestCases,n=0;
while (n!=nTestCases)
{
	n++;

	int r,c,w, count = 0, enoughspaces = 0;
	std::cin>>r>>c>>w;
	int currpos = w-1;
	bool gameover = false;

	int ** arr = 0;
	arr = new int *[r];
	for( int i = 0 ; i < r ; i++ )
		arr[i] = new int[c];

	while(!gameover)
	{

		count ++;
		arr[0][currpos] = 1;

		enoughspaces = c-1-currpos;
		if(enoughspaces < w)
		{
			gameover = true;
		}
		else
		{
			currpos = currpos + w;
		}

	}
	if(enoughspaces == 0 )
		count = count + (w-1);
	else if(enoughspaces > 0)
		count = count + w;



	std::cout<<"Case #"<<n<<": "<<count<<std::endl;
}
//for( int i = 0 ; i < r ; i++ )
//    delete [] arr[i] ;
//delete [] arr ;
//std::cin.rdbuf(cinbuf);
//std::cout.rdbuf(coutbuf);
}
