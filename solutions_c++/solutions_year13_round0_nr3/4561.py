import math


def is_palindrome ( x ) :
  a = []
  while ( x > 0 ):
    a.append ( x % 10 )
    x /= 10
  leng = len(a) 
  for i in range ( leng ):
    if a[i] != a[leng-1-i] :
      return False
  return True

MMM = 2001003
f = open ( 'table.out', 'wb' )
for i in range(MMM) :
  if is_palindrome ( i ) and is_palindrome ( i ** 2 ):
    f.write( str (i ** 2 ) + '\n' )
