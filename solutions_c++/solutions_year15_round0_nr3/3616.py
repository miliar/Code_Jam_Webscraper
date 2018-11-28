#include <iostream>
#include <vector>

using namespace std;

struct number {
	char num;
	int flag;
};

bool is_i(struct number x) {
	return (x.flag==1 && x.num=='i');
}

bool is_j(struct number x) {
	return (x.flag==1 && x.num=='j');
}

bool is_k(struct number x) {
	return (x.flag==1 && x.num=='k');
}

bool is_1(struct number x) {
	return (x.flag==1 && x.num=='1');
}

struct number multi(struct number x, struct number y) {
	struct number z;

	z.flag = x.flag*y.flag;

	if (x.num=='1') {
		z.num = y.num;
	} else if (y.num=='1') {
		z.num = x.num;
	} else if (x.num=='i' && y.num=='i') {
		z.num = '1';
		z.flag = -1*z.flag;
	} else if (x.num=='i' && y.num=='j') {
		z.num = 'k';
	} else if (x.num=='i' && y.num=='k') {
		z.num = 'j';
		z.flag = -1*z.flag;
	} else if (x.num=='j' && y.num=='i') {
		z.num = 'k';
		z.flag = -1*z.flag;
	} else if (x.num=='j' && y.num=='j') {
		z.num = '1';
		z.flag = -1*z.flag;
	} else if (x.num=='j' && y.num=='k') {
		z.num = 'i';
	} else if (x.num=='k' && y.num=='i') {
		z.num = 'j';
	} else if (x.num=='k' && y.num=='j') {
		z.num = 'i';
		z.flag = -1*z.flag;
	} else if (x.num=='k' && y.num=='k') {
		z.num = '1';
		z.flag = -1*z.flag;
	}

	return z;
}

int main() {
	FILE *fp = fopen("C-small-attempt1.in","r");
	//FILE *fp = fopen("test.txt","r");
	int T = 0;
	fscanf(fp, "%d", &T);
	//fread(&T,sizeof(int),1,fp);
	for (int i=1;i<=T;i++) {
		printf("Case #%d: ", i);
		
		int L,X;
		fscanf(fp, "%d %d\n", &L, &X);

		std::vector<char> myvector (L);

		for (int j=0;j<L;j++) {
			char c;
			fread(&c,sizeof(char),1,fp);
			myvector[j] = c;// - '0';
		}
		
		//start: to determine y
		//int high_o = 0,low_o = 0;
		struct number holding_num;
		holding_num.flag = 1;
		holding_num.num = '1';

		int state = 0;
		bool can = false;
		for (int high_o = 0;high_o<X;high_o++) {
			for (int low_o = 0;low_o<L;low_o++) {
				if (state==0) {//still checking i
					struct number current_num;
					current_num.flag = 1;
					current_num.num = myvector[low_o];

					holding_num = multi(holding_num,current_num);
					if (is_i(holding_num)) {
						//reset holding_num
						holding_num.flag = 1;
						holding_num.num = '1';

						//jump state
						state++;
					}
				} else if (state==1) { //now check j
					struct number current_num;
					current_num.flag = 1;
					current_num.num = myvector[low_o];

					holding_num = multi(holding_num,current_num);
					if (is_j(holding_num)) {
						//reset holding_num
						holding_num.flag = 1;
						holding_num.num = '1';

						//jump state
						state++;
					}
				} else if (state==2) { //now check k
					struct number current_num;
					current_num.flag = 1;
					current_num.num = myvector[low_o];

					holding_num = multi(holding_num,current_num);
					if (is_k(holding_num)) {
						//reset holding_num
						holding_num.flag = 1;
						holding_num.num = '1';

						//jump state
						state++;
					}
				} else if (state==3) { //now check 1
					struct number current_num;
					current_num.flag = 1;
					current_num.num = myvector[low_o];

					holding_num = multi(holding_num,current_num);
					
					//if (is_1(holding_num)) {
						/*
						//reset holding_num
						holding_num.flag = 1;
						holding_num.num = '1';

						//jump state
						state++;
						*/
					//}
				}

				if (high_o==X-1 && low_o==L-1) {
					if (state<2) {
						can = false;
					} else if (state==2) {
						can = is_k(holding_num);
					} else if (state==3) {
						can = is_1(holding_num);
					}
				}
				
			}
		}

		/*
		if (myvector[offset]=='i')




		int i_cant=0, j_cant=0, k_cant=0;
		bool end = false; 
		int offset = 0;
		while (!end) {
			if (i_cant==1 || j_cant==1 || k_cant==1) {
				break;
			}

			if (i_cant==0) {
				if (myvector[offset]=='i') {

				} else {
				}
			} else if (j_cant==0) {

			} else {
				//check remaining = 1
			}

			offset++;
			if (offset == L)
				end = true;
		}
		*/
		
		//end
		
		if (can)
			printf("YES");
		else
			printf("NO");

		if (i!=T)
			printf("\n");
	}
	
	return 0;
}