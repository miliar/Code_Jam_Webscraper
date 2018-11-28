#include<iostream>
#include<algorithm>
#include<fstream>

bool check_status(const int arr[], int size, int val){
	while(--size>=0 && arr[size]==val);
	if (size==-1)
		return true;
	else
		return false;
}


int last_number(int no){
	if (no == 0)
		return -1;
	int status[10];
	int digit;
	int place=10;
	int no_copy=no;
	int i=1;
	std::fill_n(status,10,0);
	while(true){
		do{
			digit=no_copy%place;
			switch(digit){
				case 0:
					status[0]=1;
					break;
				case 1:
					status[1]=1;
					break;
				case 2:
					status[2]=1;
					break;
				case 3:
					status[3]=1;
					break;
				case 4:
					status[4]=1;
					break;
				case 5:
					status[5]=1;
					break;
				case 6:
					status[6]=1;
					break;
				case 7:
					status[7]=1;
					break;
				case 8:
					status[8]=1;
					break;
				case 9:
					status[9]=1;
					break;
			}
			no_copy=no_copy/10;
		}while(no_copy!=0);
		if(check_status(status,10,1))
			return no*i;
		i++;
		no_copy=no*(i);
	}

}

int main(void)
{
	using namespace std;
	ifstream ifile("input");
	ofstream ofile("output");
	int total_case,no,lno;
	ifile>>total_case;
	for(int i=1;i<=total_case;i++){
		ifile>>no;
		lno=last_number(no);
		if (lno==-1)
			ofile<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
		else
			ofile<<"Case #"<<i<<": "<<lno<<endl;
	}
	/* int no; */
	/* cin>>no; */
	/* cout<<endl<<last_number(no)<<endl; */
	return 0;
}
