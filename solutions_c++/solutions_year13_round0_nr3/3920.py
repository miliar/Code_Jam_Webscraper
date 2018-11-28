#include<iostream>
#define MAXDIGITS 500
using namespace std;

class largenumber{
public:
  int digits[MAXDIGITS];
  int start;
  int end;


  largenumber(){
    start=end=MAXDIGITS/2;
  }

  //  ~largenumber(){
  //    delete digits;
  //  }

  largenumber(const largenumber& value){
    start=value.start;
    end=value.end;
    for(int i=start;i<end;i++)
      digits[i]=value.digits[i];
  }

  static largenumber fromInt(int value){
    largenumber ans=largenumber();
    while(value>0){
      ans.appendFirstDigit(value%10);
      value/=10;
    }
    return ans;
  }

  void add(const largenumber& number);
  void subtract(const largenumber& number);
  //assumes result is positive!
  
  void mult(int d);
  //inefficient - use for small d only

  void appendLastDigit(int d);
  void appendFirstDigit(int d);
  void print() const;

  void trimleading0();

  long long toint();
  //use only for debugging!
};

void largenumber::print() const{
  for(int i=start;i<end;i++)
    cout<<digits[i];
}

long long largenumber::toint(){
  long long answer=0;
  for(int i=start;i<end;i++)
    answer=10*answer+digits[i];
  return answer;
}

void largenumber::appendLastDigit(int d){
  digits[end++]=d;
}

void largenumber::appendFirstDigit(int d){
  digits[--start]=d;
}

void largenumber::add(const largenumber& number){
  int index;
;
  for(int k=number.end-1; k>=number.start; k--){
    index=k+end-number.end; //the decimal place corresponding to k
    if(index<start){
      appendFirstDigit(0);
    }
    digits[index]+=number.digits[k];
    if(digits[index]>=10){
      digits[index]-=10;
      int l=index-1;
      while(l>=start && digits[l]==9){
	digits[l]=0;
	l--;
      }
      if(l<start)
	appendFirstDigit(0);
      digits[l]++;
    }
  }          
}

void largenumber::subtract(const largenumber& number){
  //assumes result is positive!
  int index;
  for(int k=number.start;k<number.end;k++){
    index= k+end-number.end;
    digits[index]-=number.digits[k];
    if(digits[index]<0){
      digits[index]+=10;
      int l=index-1;
      while(digits[l]==0)
	digits[l--]=9;
      digits[l]--;
    }
  }

  //trim leading zeros
  trimleading0();
  while(digits[start]==0)
    start++;
}

void largenumber::trimleading0(){
  while(digits[start]==0)
    start++;
}

void largenumber::mult(int d){
  largenumber* copy= new largenumber(*this);
  if(d==0)
    subtract(*copy);
  else{
    while(d>1){
      add(*copy);
      d--;
    }
  }
  delete copy;
}

bool isPalin(const largenumber& number){
  for(int i=number.start;i<number.end;i++)
    if(number.digits[i]!=number.digits[number.end-1+number.start-i])
      return false;
  return true;
}

void testLargeNumber();


class palinstarter{
public:

  largenumber front, back,
    frontsq, backsq, frontback;
  int length;
  
  palinstarter(){
    length=0;
  }

  palinstarter(const palinstarter& value): front(value.front),
					   back(value.back),
					   backsq(value.backsq),
					   frontsq(value.frontsq),
					   frontback(value.frontback),
					   length(value.length){
  };

  
  void extend(int d);
  bool valid();
  //void backtrack();
};

void palinstarter::extend(int d){
  largenumber dF= largenumber(front);
  dF.mult(d);
  

  largenumber dB=largenumber(back);
  dB.mult(d);
  
  largenumber dsq=largenumber::fromInt(d*d);
 
 
  //frontsq=100frontsq+20ddF+d^2
  frontsq.appendLastDigit(0);
  frontsq.appendLastDigit(0);
  dF.appendLastDigit(0);
  frontsq.add(dF);
  frontsq.add(dF);
  frontsq.add(dsq);



  //note that dF=10dF now!
  for(int i=0;i<length;i++){
    dF.appendLastDigit(0);
  }
  //and now dF=10^(l+1)d front



   for(int i=0;i<length ;i++)
     dsq.appendLastDigit(0);
  //and dsq=d*d*10^(l)


  frontback.appendLastDigit(0);
  frontback.add(dF);
  frontback.add(dB);
  frontback.add(dsq);
  // fB -> 10fb+ 10^(l+1) fd+ db+ 10^(l)d^2

  for(int i=0;i<length;i++){
    dsq.appendLastDigit(0);
    dB.appendLastDigit(0);
  }
  // dsq= 10^(2l) d^2
  //db = 10^l db

  backsq.add(dB);
  backsq.add(dB);
  backsq.add(dsq);
  //backsq -> bs + 2 10^l dB +10^2l d^2

  back.appendFirstDigit(d);
  front.appendLastDigit(d);
  length++;

  frontsq.trimleading0();
  backsq.trimleading0();
  frontback.trimleading0();

}

int reversematch(const largenumber& num1, const largenumber& num2){
  int k=0;
  while(k+num1.start<num1.end &&
	num2.end-1-k>=num2.start&&
	num1.digits[k+num1.start]==num2.digits[num2.end-1-k])
    k++;
  return k;
}

int match(const largenumber& num1, const largenumber& num2){
  int k=0;
  while(k+num1.start<num1.end &&
	k+num2.start<num2.end&&
	num1.digits[k+num1.start]==num2.digits[num2.start+k])
    k++;
  return k;
}

bool palinstarter::valid(){

  largenumber fplus1sq = largenumber(frontsq);
  fplus1sq.add(front);
  fplus1sq.add(front);
  fplus1sq.add(largenumber::fromInt(1));

  bool checktop=true;
  bool checkbottom=true;

  int top,middle, bottom;

  for(int l=0; l<length;l++){
    top=fplus1sq.digits[fplus1sq.start+l];
    middle=backsq.digits[backsq.end-1-l];
    bottom=frontsq.digits[frontsq.start+l];

    if(checktop){
      if(top<middle)
	return false;
      checktop=(top==middle);
    }
    if(checkbottom){
      if(middle<bottom)
	return false;
      checkbottom=(middle==bottom);
    }
  }

  return true;
}

void printStarter(palinstarter& starter){
  cout<<endl<<endl<<endl;
  cout<<"Front: ";
  starter.front.print();
  cout<<endl<<"Back: ";
  starter.back.print();
  cout<<endl<<"FrontSq: ";
  starter.frontsq.print();
  cout<<endl<<"BackSq: ";
  starter.backsq.print();
  cout<<endl<<"FrontBack: ";
  starter.frontback.print();
  cout<<endl<<"length: "<<starter.length<<endl;
  cout<<"VALID:"<<starter.valid()<<endl;
}

void testPalinStarter();

largenumber concatenate(const palinstarter& starter){
  largenumber frontsq= largenumber(starter.frontsq);
  largenumber frontback= largenumber(starter.frontback);
  for(int i=0;i<starter.length*2; i++)
    frontsq.appendLastDigit(0);
  for(int i=0;i<starter.length; i++)
    frontback.appendLastDigit(0);

  frontsq.add(frontback);
  frontsq.add(frontback);
  frontsq.add(starter.backsq);
  return frontsq;
}

largenumber concatenateOdd(const palinstarter& starter, int d){
  largenumber frontsq= largenumber(starter.frontsq);
  largenumber frontback= largenumber(starter.frontback);
  for(int i=0;i<starter.length*2+2; i++)
    frontsq.appendLastDigit(0);
  for(int i=0;i<starter.length+1; i++)
    frontback.appendLastDigit(0);

  frontsq.add(frontback);
  frontsq.add(frontback);
  frontsq.add(starter.backsq);
  if(d!=0){
    largenumber dsq=largenumber::fromInt(d*d);
    for(int i=0;i<starter.length*2;i++)
      dsq.appendLastDigit(0);
    frontsq.add(dsq);
    largenumber sum=starter.front;
    for(int i=0;i<starter.length+1;i++)
      sum.appendLastDigit(0);
    sum.add(starter.back);
    sum.mult(d);
    frontsq.add(sum);
  }

  return frontsq;

}


const int MAXT=1005;
long long faircounter[MAXT], low[MAXT], high[MAXT];
int T;

void addFair(long long f){
  for(int t=0;t<T;t++){
    if(low[t]<=f && f<=high[t])
      faircounter[t]++;
  }
}


void findFair(const palinstarter& starter){
  largenumber fair=concatenate(starter);
  if(isPalin(fair)){
    addFair(fair.toint());
  }

  for(int d=0;d<10;d++){
    fair=concatenateOdd(starter,d);
    if(isPalin(fair)){
      addFair(fair.toint());
    }
  }
}

void dfs(palinstarter starter, int d, int maxdepth){
  starter.extend(d);
  if(!starter.valid()|| starter.length>maxdepth)
    return;
  findFair(starter);
  for(int i=0; i<9;i++)
    dfs(starter, i, maxdepth);
}
int main(){
 
  cin>>T;
  for(int t=0;t<T;t++){
    faircounter[t]=0;
    cin>>low[t]>>high[t];
  }

  addFair(1);
  addFair(4);
  addFair(9);

  int depth=10;
  for(int d=1;d<10;d++)
    dfs(palinstarter(),d,depth);

  for(int t=0;t<T;t++)
    cout<<"Case #"<<t+1<<": "<<faircounter[t]<<endl;




}


void testLargeNumber(){
  largenumber number=largenumber();
  number.appendFirstDigit(3);
  number.appendFirstDigit(4);
  number.appendFirstDigit(6);
  number.print();
  cout<<endl;
  if(number.toint()!=643)
    cout<<"Error!"<<endl;
  number.appendLastDigit(5);

  number.print();
  cout<<endl;
  if(number.toint()!=6435)
    cout<<"Error!"<<endl;

 

  largenumber copy=largenumber(number);
  if(copy.toint()!=6435)
    cout<<"Error!"<<endl;

  copy.appendLastDigit(3);
  if(copy.toint()!=64353)
    cout<<"Error!"<<endl;
  if(number.toint()!=6435)
    cout<<"Error!"<<endl;


  number.add(copy);
  cout<<"Sum: ";
  number.print();
  cout<<endl;
  if(number.toint()!=6435+64353)
    cout<<"Error!"<<endl;

  number.add(copy);
  cout<<"Sum: ";
  number.print();
  cout<<endl;
  if(number.toint()!=6435+2*64353)
    cout<<"Error!"<<endl;

  number.add(copy);
  cout<<"Sum: ";
  number.print();
  cout<<endl;
  if(number.toint()!=6435+3*64353)
    cout<<"Error!"<<endl;
  
  number.subtract(copy);
  cout<<"Sub: ";
  number.print();
  cout<<endl;
  if(number.toint()!=6435+2*64353)
    cout<<"Error!"<<endl;

  largenumber number1=largenumber();
  number1.appendLastDigit(1);
  number1.appendLastDigit(0);
  number1.appendLastDigit(0);
  number1.appendLastDigit(0);
  number1.appendLastDigit(0);
  number1.appendLastDigit(0);

  largenumber number2=largenumber();
  number2.appendLastDigit(2);
  number2.appendLastDigit(3);

  number1.subtract(number2);
  number1.print();
  cout<<endl;

  if(number1.toint()!=99977)
    cout<<"Error!"<<endl;

  largenumber number3=largenumber::fromInt(745063);
  if(number3.toint()!=745063)
    cout<<"Error!"<<endl;

  number3.mult(7);
  if(number3.toint()!=745063*7)
  cout<<"Error!"<<endl;

  largenumber number4=largenumber::fromInt(99999);
  number4.add(largenumber::fromInt(1));
  number4.print();
  cout<<endl;
}

void testPalinStarter(){
  palinstarter starter=palinstarter();
  printStarter(starter);
  starter.extend(3);
  printStarter(starter);
  starter.extend(4);
  printStarter(starter);
  starter.extend(7);
  printStarter(starter);
  starter.extend(9);
  printStarter(starter);
  starter.extend(5);
  printStarter(starter);
 
  palinstarter starter2=palinstarter();
  starter2.extend(1);
  starter2.extend(0);
  printStarter(starter2);
}



