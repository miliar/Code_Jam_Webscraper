#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>


bool isFeasible()
{
	return true;
}
void mult(int a, int b, int &c, int &sign)
{
	switch (a){
		case 1: c = b; break;
		case 'i': 
			{
				if (b == 1){
					c = 'i';
				}
				else if (b == 'i'){
					c = 1;
					sign *= -1;
				}
				else if (b == 'j'){
					c = 'k';
				}
				else if (b == 'k'){
					c = 'j';
					sign *= -1;
				}
			}
			break;
		case 'j': 
			{
				if (b == 1){
					c = 'j';
				}
				else if (b == 'i'){
					c = 'k';
					sign *= -1;
				}
				else if (b == 'j'){
					c = 1;
					sign *= -1;
				}
				else if (b == 'k'){
					c = 'i';
				}
			}
			break;
		case 'k': 
			{
				if (b == 1){
					c = 'k';
				}
				else if (b == 'i'){
					c = 'j';
				}
				else if (b == 'j'){
					c = 'i';
					sign *= -1;
				}
				else if (b == 'k'){
					c = 1;
					sign *= -1;
				}
			}
			break;
	}
}

void findProduct(std::string &str, 
std::vector<int> &product, 
std::vector<int> &productSign
)
{
	int c = 1, sign =1;
	//printf ("\n");
	for (size_t i = 0; i != str.size(); i++){
		mult(c, str[i], c, sign);
		product.push_back(c);
		productSign.push_back(sign);
		//printf("\t\t Sign %d, %c", sign, (char)c);
	}
}
void solve(int caseNo)
{
	int L, X;
	char a[8192*2];
	std::string str;
	scanf("%d %d %s", &L, &X, a);
	str = "";

	for (int i = 0; i != X; i++){
		str += a;
	}

	/*bool found = false;
	if (!isFeasible()){
		if (caseNo > 1)
			printf("\n");
		printf("Case #%d: NO", caseNo);
	}*/
	std::vector<int> product; 
	std::vector<int> productSign;
	findProduct(str, product, productSign);
	//findILocation(str, iLocVec);
	//findKLocation(str, kLocVec);
	bool iFound = false, kFound = false;
	int iPos = 0, kPos = 0;
	if (product[str.size()-1] != 1 || productSign[str.size()-1] != -1 ){
		if (caseNo > 1)
			printf("\n");
		printf("Case #%d: NO", caseNo);
		return;
	}
	
	for (size_t i = 0; i != (str.size()-2); i++){
		if (product[i] == 'i' && productSign[i] == 1){
			iFound = true;
			iPos = i;
			break;
		}
	}
	for (size_t i = iPos+1; i != (str.size()-1) && iFound; i++){
		if (product[i] == 'k' && productSign[i] == 1){
			kFound = true;
			kPos = i;
			break;
		}
	}

	if (caseNo > 1)
		printf("\n");
	if (kFound)
		printf("Case #%d: YES", caseNo);
	else
		printf("Case #%d: NO", caseNo);
}

int main()
{
	int numOfTestCases, i;
	scanf("%d", &numOfTestCases);
	for (i = 0; i < numOfTestCases; i++){
		solve(i+1);
	}
}
